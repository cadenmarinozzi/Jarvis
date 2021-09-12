from datetime import datetime
import random

def _time(textToSpeech, phrases, text):
    textString = "";
    place = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) and "" or " ");
        
    for phrase in phrases["now"]:
        if (phrase in textString):
            textString = textString.replace(phrase, "");

    for phrase in phrases["placeIdentifiers"]:
        if (phrase in textString):
            place = textString.split(phrases["placeIdentifiers"][phrase])[1];

            break;

    randomAnswerNow = random.randint(0, len(phrases["answerNow"]) - 1);
    answerNow = list(phrases["answerNow"])[randomAnswerNow];
    time = datetime.now().strptime(datetime.now().time().strftime("%H:%M"), "%H:%M").strftime("%I:%M %p");
    speechString = answerNow + " " + time;
    textToSpeech(speechString);