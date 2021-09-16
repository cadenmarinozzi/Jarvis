import json, requests
from simpleSound import play
from lib.Speech.speechToText import speechToText
from lib.Speech.textToSpeech import TextToSpeech
from lib.Utilities.webSockets import websocketServer
from processing import Processor

ip = "192.168.4.70";
server = websocketServer(ip, 8080);
file = open("configuration.json");
fileContents = file.read();
configuration = json.loads(fileContents);
ibm_watson_token = configuration["ibm_watson"]["token"];
textToSpeech = TextToSpeech(ibm_watson_token, play, server, False);
processor = Processor(textToSpeech.textToSpeech);

while (True):
    response = speechToText();
    processor.process(response);