from newsapi import NewsApiClient
import json, re

file = open("configuration.json");
fileContents = file.read();
configuration = json.loads(fileContents);
newsapi_api_key = configuration["newsapi"]["api_key"];
newsapi = NewsApiClient(api_key = newsapi_api_key);

def news(textToSpeech, phrases, text):
    news = [];
    textString = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) - 1 and "" or " ");

    amount = re.search(re.compile("([0-9])"), textString);

    if (amount):
        amount = int(amount.group(0));
    else:
        amount = 5;

    if ("headlines" in textString or "top" in textString):
        headlines = newsapi.get_top_headlines(country = "us", language = "en");
        articles = headlines["articles"];

        for index, article in enumerate(articles):
            title = article["title"];
            news.append(title);

            if (index == amount - 1):
                break;
    else:
        everything = newsapi.get_everything(country = "us", language = "en");
        articles = everything["articles"];

        for index, article in enumerate(articles):
            title = article["title"];
            news.append(title);

            if (index == amount - 1):
                break;

    textToSpeech("The top " + str(amount) + " headlines for today are");

    for title in news:
        textToSpeech(title);