from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1";

from lib.Modules.time import _time
from lib.Modules.greet import greet
from lib.Modules.date import day, week, month, year, date
from lib.Modules.ip import ip
from lib.Modules.shutdown import shutdown
from lib.Modules._wikipedia import _wikipedia
from lib.Modules.news import news
from lib.Modules.internetSpeed import upload, download
from lib.Modules.system import cpu, ram
from lib.Modules.weather import weather, temperature, airPressure, windSpeed, humidity
from lib.Modules.joke import joke
from lib.Modules.wolfram_alpha import wolfram
from lib.Modules.music import *
from datetime import datetime
from lib.Modules.wakeup import wakeup
from lib.Modules.alarm import *
import json, _thread, pygame, random, os, time
import lib.Modules.wakeup

pygame.init();
pygame.mixer.init();
file = open("lib/Speech/phrases.json", "r");
fileContents = file.read();
file.close();
phrases = json.loads(fileContents);
file = open("configuration.json");
fileContents = file.read();
configuration = json.loads(fileContents);
wakeupTime = configuration["wakeupTime"];
sendToWebsocket = configuration["send_to_websocket"];
prefixes = {
    "jarvis",
    "arvest",
    "harvest",
    "garvis"
};

modules = {
    "time": _time,
    "day": day,
    "week": week,
    "month": month,
    "year": year,
    "date": date,
    "ip": ip,
    "shutdown": shutdown,
    "wikipedia": _wikipedia,
    "news": news,
    "upload": upload,
    "download": download,
    "ram": ram,
    "cpu": cpu,
    "weather": weather,
    "temperature": temperature,
    "air pressure": airPressure,
    "wind speed": windSpeed,
    "humidity": humidity,
    "joke": joke,
    "play": play,
    "pause": pause,
    "unpause": unpause,
    "restart": restart,
    "stop": stop,
    "volume": volume,
    "mute": mute,
    "add": addAlarm,
    "remove": removeAlarm
};

class Processor():
    def __init__(self, textToSpeech, sms, number):
        self.textToSpeech = textToSpeech;
        self.sms = sms;
        self.number = number;

        try:
            self.lastSMS = sms.receive(number)[0];
        except:
            self.lastSMS = "";

    def process(self, text):
        text = text.lower();
        tokens = self.tokenize(text);
        location = 0;
        prefixed = False;
        commandFound = False;

        for prefix in prefixes:
            if (prefix in tokens):
                prefixed = True;

        if (prefixed):
            while (not commandFound and location < len(tokens)):
                if (tokens[location] in phrases["greetings"]):
                    if (len(tokens) < 3):
                        greet(self.textToSpeech, phrases, tokens);
                        commandFound = True;

                        break;
                    else:
                        location += 1;

                try:
                    if (tokens[location + 1] in phrases["questionIdentifiers"]):
                        location += 2;

                        if (tokens[location] in modules):
                            module = modules[tokens[location]];
                            module(self.textToSpeech, phrases, tokens);
                            commandFound = True;

                            break;
                except:
                    errored = True;

                if (tokens[location] in modules):
                    module = modules[tokens[location]];
                    module(self.textToSpeech, phrases, tokens);
                    commandFound = True;

                    break;

                location += 1;   

            if (not commandFound):
                wolfram(self.textToSpeech, phrases, tokens);

    def tokenize(self, text):
        tokens = [];
        words = text.split(" ");

        for word in words:
            tokens.append(word);

        return tokens;

    def handleWakeup(self):
        def wakeupThread(threadName, delay):
            while (True):
                _time = datetime.now().strptime(datetime.now().time().strftime("%H:%M"), "%H:%M").strftime("%#I:%#M %p");

                if (_time == wakeupTime):
                    dirFiles = os.listdir("Bin/");
                    files = [];

                    for file in dirFiles:
                        if (".mp3" in file or ".wav" in file):
                            files.append(file);

                    filesLength = len(files);
                    chosen = random.randint(0, filesLength - 1);
                    file = files[chosen];
                   
                    if (sendToWebsocket):
                        file = open("Bin/" + file, "rb");
                        fileContents = file.read();
                        encoded = base64.b64encode(fileContents);
                        self.server.send_message_to_all(encoded);
                        file.close();  

                    pygame.mixer.music.load("Bin/" + file);
                    pygame.mixer.music.play();
                    time.sleep(25);
                    pygame.mixer.music.fadeout(5000);
                    wakeup(self.textToSpeech, phrases);

        _thread.start_new_thread(wakeupThread, ("Thread-4", 1, ));

    def handleAlarms(self):
        def alarmThread(threadName, delay):
            while (True):
                _time = datetime.now().strptime(datetime.now().time().strftime("%H:%M:%S"), "%H:%M:%S").strftime("%#I:%#M:%#S %p");
                file = open("data.json");
                fileContents = file.read();
                data = json.loads(fileContents);
                file.close();
                alarms = data["alarms"];

                for alarm in alarms:
                    if (alarm["time"] == _time):
                        dirFiles = os.listdir("Bin/");
                        files = [];

                        for file in dirFiles:
                            if (".mp3" in file or ".wav" in file):
                                files.append(file);

                        filesLength = len(files);
                        chosen = random.randint(0, filesLength - 1);
                        file = files[chosen];
                         
                        if (sendToWebsocket):
                            file = open("Bin/" + file, "rb");
                            fileContents = file.read();
                            encoded = base64.b64encode(fileContents);
                            self.server.send_message_to_all(encoded);
                            file.close();  
                            
                        pygame.mixer.music.load("Bin/" + file);
                        pygame.mixer.music.play();
                        time.sleep(25);
                        pygame.mixer.music.fadeout(5000);

        _thread.start_new_thread(alarmThread, ("Thread-5", 1, ));

    def handleSMS(self):
        def smsThread(threadName, delay):
            while (True):
                messages = self.sms.receive(self.number);
                message = messages[0];
                    
                try:
                    lastMessage = message.body;
                except:
                    lastMessage = "";

                if (lastMessage != self.lastSMS):
                    self.textToSpeech("You have a text message from" + message.from_.replace("", " "));
                    self.textToSpeech(lastMessage);
                    self.lastSMS = lastMessage;

        _thread.start_new_thread(smsThread, ("Thread-2", 1, ));