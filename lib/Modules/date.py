from datetime import datetime
from lib.Utilities.suffix import suffixNumber
import random, math

def day(textToSpeech, phrases, text):
    day = datetime.now().strftime("%#d");
    numberSuffix = suffixNumber(int(day));
    randomDateNow = random.randint(0, len(phrases["answerDateNow"]) - 1);
    dateNow = list(phrases["answerDateNow"])[randomDateNow];
    textToSpeech(dateNow + " " + day + numberSuffix);

def week(textToSpeech, phrases, text):
    day = int(datetime.now().strftime("%#d"));
    week = math.ceil(day / 7);
    month = datetime.now().strftime("%B");
    numberSuffix = suffixNumber(week);
    randomDateNow = random.randint(0, len(phrases["answerDateNow"]) - 1);
    dateNow = list(phrases["answerDateNow"])[randomDateNow];
    textToSpeech(dateNow + " " + str(week) + numberSuffix + " week of " + month);

def month(textToSpeech, phrases, text):
    month = datetime.now().strftime("%B");
    randomDateNow = random.randint(0, len(phrases["answerNow"]) - 1);
    dateNow = list(phrases["answerNow"])[randomDateNow];
    textToSpeech(dateNow + " " + month);

def year(textToSpeech, phrases, text):
    year = datetime.now().strftime("%Y");
    textToSpeech("It is " + year);

def date(textToSpeech, phrases, text):
    date = datetime.now().strftime("%#m/%#d/%Y");
    textToSpeech("The date is " + date);
                                    