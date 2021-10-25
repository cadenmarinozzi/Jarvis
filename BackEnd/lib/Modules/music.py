# this file needs a MAJOR makeover
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1";

import pygame, re, requests, sys, urllib.parse, urllib.request, pafy, os, json, base64
import moviepy.editor as mp
from bs4 import BeautifulSoup

pygame.init();
pygame.mixer.init();
file = open("configuration.json");
fileContents = file.read();
configuration = json.loads(fileContents);
sendToWebsocket = configuration["sendToWebsocket"];
playLocal = configuration["playLocal"];

def play(textToSpeech, phrases, text, server):
    textString = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) - 1 and "" or " ");

    song = textString.split(" play ")[1];
    speechString = "Give me a moment to search for " + song;
    textToSpeech(speechString);
    results = re.findall(r"watch\?v=(\S{11})", urllib.request.urlopen("https://www.youtube.com/results?" + urllib.parse.urlencode({
        "search_query": song
    })).read().decode());
    inspect = BeautifulSoup(requests.get("https://www.youtube.com/watch?v=" + "{}".format(results[index])).content, "html.parser");
    
    for concatMusic in inspect.find_all("meta", property = "og:title"):
        pass;
        
    pafy.new("https://www.youtube.com/watch?v=" + "{}".format(results[index])).getbest().download("Temp\\music.mp4");
    mp.VideoFileClip("Temp\\music.mp4").audio.write_audiofile("Temp\\result.wav");
    os.remove("Temp\\music.mp4");
    speechString = "Now playing " + concatMusic["content"];
    textToSpeech(speechString);

    if (sendToWebsocket): # send as wav for this (param in websocket send)
        file = open("Temp\\result.wav", "rb");
        fileContents = file.read();
        encoded = base64.b64encode(fileContents);
        server.send_message_to_all(encoded);
        file.close();  

    if (playLocal):
        pygame.mixer.music.load("Temp\\result.wav");
        pygame.mixer.music.play();

def restart(textToSpeech, phrases, text, server):
    pygame.mixer.music.stop();
    pygame.mixer.music.play();

def stop(textToSpeech, phrases, text, server):
    pygame.mixer.music.stop();

def pause(textToSpeech, phrases, text, server):
    pygame.mixer.music.pause();

def unpause(textToSpeech, phrases, text, server):
    pygame.mixer.music.unpause();

def restart(textToSpeech, phrases, text, server):
    pygame.mixer.music.unpause();

def volume(textToSpeech, phrases, text, server):
    textString = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) - 1 and "" or " ");

    volume = re.search(re.compile("([0-9])"), textString);
    
    if ("decrease" in textString or "down" in textString):
        currentVolume = pygame.mixer.music.get_volume();
        pygame.mixer.music.set_volume(currentVolume - volume / 100);
    elif ("increase" in textString or "up" in textString):
        currentVolume = pygame.mixer.music.get_volume();
        pygame.mixer.music.set_volume(currentVolume + volume / 100);
    else:
        volume = re.search(re.compile("([0-9])"), textString);
        pygame.mixer.music.set_volume(volume / 100);

def mute(textToSpeech, phrases, text, server):
    pygame.mixer.music.set_volume(0);