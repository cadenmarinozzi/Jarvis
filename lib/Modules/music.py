# this file needs a MAJOR makeover
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1";

import pygame, re, requests, sys, urllib.parse, urllib.request, pafy, os
import moviepy.editor as mp
from bs4 import BeautifulSoup

pygame.init();
pygame.mixer.init();

def play(textToSpeech, phrases, text):
    textString = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) and "" or " ");

    song = textString.split(" play ")[1];
    textToSpeech("Give me a moment to search for " + song);
    results = re.findall(r"watch\?v=(\S{11})", urllib.request.urlopen("https://www.youtube.com/results?" + urllib.parse.urlencode({
        "search_query": song
    })).read().decode());
    inspect = BeautifulSoup(requests.get("https://www.youtube.com/watch?v=" + "{}".format(results[index])).content, "html.parser");
    
    for concatMusic in inspect.find_all("meta", property = "og:title"):
        pass;
        
    pafy.new("https://www.youtube.com/watch?v=" + "{}".format(results[index])).getbest().download("Temp\\music.mp4");
    mp.VideoFileClip("Temp\\music.mp4").audio.write_audiofile("Temp\\result.wav");
    os.remove("Temp\\music.mp4");
    textToSpeech("Now playing " + concatMusic["content"]);
    pygame.mixer.music.load("Temp\\result.wav");
    pygame.mixer.music.play();

def restart(textToSpeech, phrases, text):
    pygame.mixer.music.stop();
    pygame.mixer.music.play();

def stop(textToSpeech, phrases, text):
    pygame.mixer.music.stop();

def pause(textToSpeech, phrases, text):
    pygame.mixer.music.pause();

def unpause(textToSpeech, phrases, text):
    pygame.mixer.music.unpause();

def restart(textToSpeech, phrases, text):
    pygame.mixer.music.unpause();

def volume(textToSpeech, phrases, text):
    textString = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) and "" or " ");

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

def mute(textToSpeech, phrases, text):
    pygame.mixer.music.set_volume(0);