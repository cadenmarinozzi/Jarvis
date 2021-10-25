import requests, json, pyjokes

def joke(textToSpeech, phrases, text, server):
    joke = pyjokes.get_joke();
    textToSpeech(joke);