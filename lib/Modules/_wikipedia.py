import wikipedia

def _wikipedia(textToSpeech, phrases, text):
    subject = ""; 
    textString = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) and "" or " ");

    subject = textString.split(" up ")[1].split(" on ")[0];
    result = wikipedia.summary(subject, sentences = 2);
    speechString = "The result for " + subject + " on wikipedia is " + result;
    textToSpeech(speechString);