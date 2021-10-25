from datetime import datetime
import random

def _time(textToSpeech, phrases, text, server):
    randomAnswerNow = random.randint(0, len(phrases["answerNow"]) - 1);
    answerNow = list(phrases["answerNow"])[randomAnswerNow];
    time = datetime.now().strptime(datetime.now().time().strftime("%H:%M"), "%H:%M").strftime("%I:%M %p");
    speechString = answerNow + " " + time;
    textToSpeech(speechString);