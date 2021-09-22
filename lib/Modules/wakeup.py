from datetime import datetime
from lib.Utilities.cryptoCurrency import cryptoCurrency
import requests, json, random, math

file = open("lib/Speech/phrases.json", "r");
fileContents = file.read();
file.close();
phrases = json.loads(fileContents);

def wakeup(textToSpeech, phrases):
    ethereumData = cryptoCurrency("ETH");
    price = ethereumData[0];
    priceTime = ethereumData[1];
    file = open("data.json");
    fileContents = file.read();
    file.close();
    data = json.loads(fileContents);
    lastPrice = "";

    try:
        lastPrice = data["lastPrice"];
    except:
        lastPrice = "";
        
    if (lastPrice):
        priceDelta = price - lastPrice; 

    file = open("data.json", "w");
    data["lastPrice"] = price;
    file.write(json.dumps(data));
    file.close();
    time = datetime.now().strptime(datetime.now().time().strftime("%H:%M"), "%H:%M").strftime("%I:%M %p");
    randomAnswerNow = random.randint(0, len(phrases["answerNow"]) - 1);
    answerNow = list(phrases["answerNow"])[randomAnswerNow];
    date = datetime.now().strftime("%#m/%#d/%Y");
    textToSpeech("Good morning. The date is " + date + ". " + answerNow + " " + time + " and Ethereum is at " + str(math.floor(price)) + " dollars, " + (lastPrice == "" and "" or (str(math.floor(abs(priceDelta))) + " dollars " + (priceDelta > 0 and "more" or "less") + " than yesterday.")));