import speech_recognition as sr

speechRecognizer = sr.Recognizer();

def speechToText():
    # with sr.Microphone() as source:
    #     speechRecognizer.adjust_for_ambient_noise(source, duration = 1);
    #     print("Listening...");
    #     audio = speechRecognizer.listen(source);
    #     recognized = "";
        
    #     try: 
    #         recognized = speechRecognizer.recognize_google(audio, language = "en-US");
    #     except sr.UnknownValueError:
    #         errored = True;

    #     print("transcript: " + recognized);

    #     return recognized;

    print("Listening...");
    
    return input();