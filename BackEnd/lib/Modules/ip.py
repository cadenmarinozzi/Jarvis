import requests

def ip(textToSpeech, phrases, text, server):
    ip = requests.get("https://api.ipify.org").text;
    speechString = "Your i.p is " + ip;
    textToSpeech(speechString);