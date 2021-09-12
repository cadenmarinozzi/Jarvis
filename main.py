import json
from simpleSound import play
from lib.Speech.speechToText import speechToText
from lib.Speech.textToSpeech import TextToSpeech
from processing import Processor

file = open("configuration.json");
fileContents = file.read();
configuration = json.loads(fileContents);
ibm_watson_token = configuration["ibm_watson"]["token"];
textToSpeech = TextToSpeech(ibm_watson_token, play);
processor = Processor(textToSpeech.textToSpeech);

while (True):
    response = speechToText();
    processor.process(response);