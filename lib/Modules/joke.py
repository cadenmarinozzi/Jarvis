import requests, json, pyjokes

def joke(textToSpeech, phrases, text):
    joke = pyjokes.get_joke();
    textToSpeech(joke);