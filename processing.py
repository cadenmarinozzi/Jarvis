from lib.Modules._time import _time
from lib.Modules.greet import greet
from lib.Modules.date import day, week, month, year, date
from lib.Modules.ip import ip
from lib.Modules.shutdown import shutdown
from lib.Modules._wikipedia import _wikipedia
import json

file = open("lib/Speech/phrases.json", "r");
fileContents = file.read();
file.close();
phrases = json.loads(fileContents);
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
    "wikipedia": _wikipedia
};

class Processor():
    def __init__(self, textToSpeech):
        self.textToSpeech = textToSpeech;

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

    def tokenize(self, text):
        tokens = [];
        words = text.split(" ");

        for word in words:
            tokens.append(word);

        return tokens;