import random, json

def greet(textToSpeech, phrases, text, server):
    randomGreeting = random.randint(0, len(phrases["answerGreetings"]) - 1);
    greeting = list(phrases["answerGreetings"])[randomGreeting];
    randomGreet = random.randint(0, len(phrases["answerGreet"]) - 1);
    answerGreet = list(phrases["answerGreet"])[randomGreet];
    speechString = greeting + " sir. " + answerGreet;
    textToSpeech(speechString);