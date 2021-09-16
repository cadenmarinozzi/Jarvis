import requests

def ip(textToSpeech, phrases, text):
    ip = requests.get("https://api.ipify.org").text;
    textToSpeech("Your i.p is " + ip);