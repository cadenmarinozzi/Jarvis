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
ibmWatsonToken = configuration["ibmWatson"]["token"];
ibmWatsonUrl = configuration["ibmWatson"]["serviceUrl"];
accountSID = configuration["twilio"]["accountSid"];
authToken = configuration["twilio"]["authToken"];
number = configuration["twilio"]["number"];
textToSpeech = TextToSpeech(ibmWatsonToken, ibmWatsonUrl, play, server);
client = Client(accountSID, authToken);
sms = SMS(client);
processor = Processor(textToSpeech.textToSpeech, sms, number, server);
processor.handleSMS();
processor.handleWakeup();
processor.handleAlarms();
server.set_fn_message_received(processor.handleMessage);
server.set_fn_new_client(processor.handleClient);

while (True):
    response = speechToText();
    processor.process(response);