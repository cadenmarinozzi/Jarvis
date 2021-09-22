import json, requests, socket
from simpleSound import play
from lib.Speech.speechToText import speechToText
from lib.Speech.textToSpeech import TextToSpeech
from lib.Utilities.webSockets import websocketServer
from twilio.rest import Client
from lib.Utilities.sms import SMS
from processing import Processor

hostname = socket.gethostname();
ip = socket.gethostbyname(hostname);
server = websocketServer(ip, 8080);
file = open("configuration.json");
fileContents = file.read();
configuration = json.loads(fileContents);
ibm_watson_token = configuration["ibm_watson"]["token"];
ibm_watson_url = configuration["ibm_watson"]["service_url"];
send_to_websocket = configuration["send_to_websocket"]["enabled"];
play_local = configuration["play_local"]["enabled"];
use_microphone = configuration["use_microphone"]["enabled"];
accountSID = configuration["twilio"]["account_sid"];
authToken = configuration["twilio"]["auth_token"];
number = configuration["twilio"]["number"];
textToSpeech = TextToSpeech(ibm_watson_token, ibm_watson_url, play, server, send_to_websocket, play_local);
client = Client(accountSID, authToken);
sms = SMS(client);
processor = Processor(textToSpeech.textToSpeech, sms, number);
processor.handleSMS();
processor.handleWakeup();
processor.handleAlarms();

while (True):
    response = speechToText(use_microphone);
    processor.process(response);