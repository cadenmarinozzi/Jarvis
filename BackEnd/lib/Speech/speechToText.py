import speech_recognition as sr
import json

speechRecognizer = sr.Recognizer();

def speechToText():
    respones = "";

    file = open("configuration.json");
    fileContents = file.read();
    configuration = json.loads(fileContents);

    if (configuration["useMicrophone"]):
        with sr.Microphone() as source:
            speechRecognizer.adjust_for_ambient_noise(source, duration = 1);
            print("Listening...");
            audio = speechRecognizer.listen(source);
            recognized = "";
            
            try: 
                recognized = speechRecognizer.recognize_google(audio, language = "en-US");
            except sr.UnknownValueError:
                errored = True;

            print("transcript: " + recognized);
            response = recognized;
    else:
        print("Listening...");
        response = input();
    
    return response;