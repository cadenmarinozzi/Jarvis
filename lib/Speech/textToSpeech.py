from ibm_watson import TextToSpeechV1, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import base64

class TextToSpeech():
    def __init__(self, ibm_watson_token, ibm_watson_url, play, server, sendToWebsocket, playLocal):
        authenticator = IAMAuthenticator(ibm_watson_token);
        self.textToSpeechV1 = TextToSpeechV1(authenticator = authenticator);
        self.textToSpeechV1.set_service_url(ibm_watson_url);
        self.play = play;
        self.server = server;
        self.sendToWebsocket = sendToWebsocket;
        self.playLocal = playLocal;

    def textToSpeech(self, text):
        text = text.replace("sqrt(", "square root of ");
        file = open("Temp/Speech.mp3", "wb");
        synthesized = self.textToSpeechV1.synthesize(text, voice = "en-GB_JamesV3Voice", accept = "audio/mp3").get_result().content;
        file.write(synthesized);
        file.close();
        
        if (self.playLocal):
            self.play("Temp/Speech.mp3");

        if (self.sendToWebsocket):
            file = open("Temp/Speech.mp3", "rb");
            fileContents = file.read();
            encoded = base64.b64encode(fileContents);
            self.server.send_message_to_all(encoded);
            file.close();

        print("spoke: " + text);