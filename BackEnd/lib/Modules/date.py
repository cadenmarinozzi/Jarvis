from datetime import datetime
from lib.Utilities.suffix import suffixNumber
import random, math

def day(textToSpeech, phrases, text, server):
    day = datetime.now().strftime("%#d");
    numberSuffix = suffixNumber(int(day));
    randomDateNow = random.randint(0, len(phrases["answerDateNow"]) - 1);
    dateNow = list(phrases["answerDateNow"])[randomDateNow];
    textToSpeech(dateNow + " " + day + numberSuffix);

def week(textToSpeech, phrases, text, server):
    day = int(datetime.now().strftime("%#d"));
    week = math.ceil(day / 7);
    month = datetime.now().strftime("%B");
    numberSuffix = suffixNumber(week);
    randomDateNow = random.randint(0, len(phrases["answerDateNow"]) - 1);
    dateNow = list(phrases["answerDateNow"])[randomDateNow];
    speechString = dateNow + " " + str(week) + numberSuffix + " week of " + month;
    textToSpeech(speechString);

def month(textToSpeech, phrases, text, server):
    month = datetime.now().strftime("%B");
    randomDateNow = random.randint(0, len(phrases["answerNow"]) - 1);
    dateNow = list(phrases["answerNow"])[randomDateNow];
    speechString = dateNow + " " + month;
    textToSpeech(speechString);

def year(textToSpeech, phrases, text, server):
    year = datetime.now().strftime("%Y");
    speechString = "It is " + year;
    textToSpeech(speechString);

def date(textToSpeech, phrases, text, server):
    date = datetime.now().strftime("%#m/%#d/%Y");
    speechString = "The date is " + date;
    textToSpeech(speechString);
                                    