from ibm_watson import TextToSpeechV1, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class TextToSpeech():
    def __init__(self, ibm_watson_token, play):
        authenticator = IAMAuthenticator(ibm_watson_token);
        self.textToSpeechV1 = TextToSpeechV1(authenticator = authenticator);
        self.textToSpeechV1.set_service_url("https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/e8987052-c166-4039-bdf3-1bd77aa91a32");
        self.play = play;

    def textToSpeech(self, text):
        file = open("Temp/Speech.mp3", "wb");
        synthesized = self.textToSpeechV1.synthesize(text, voice = "en-GB_JamesV3Voice", accept = "audio/mp3").get_result().content;
        file.write(synthesized);
        file.close();
        self.play("Temp/Speech.mp3");
        print("spoke: " + text);