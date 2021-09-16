import requests, json

file = open("configuration.json");
fileContents = file.read();
configuration = json.loads(fileContents);
appid = configuration["weather_api"]["appid"];

def weather(textToSpeech, phrases, text):
    textString = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) and "" or " ");

    city = "";

    for phrase in phrases["now"]:
        city = textString.split("in")[1].replace(phrase, "");

    weatherResponse = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=" + appid + "&q=" + city + "&units=imperial");
    responseJson = weatherResponse.json();
    responseCode = responseJson["cod"];

    if (responseCode == "404"):
        textToSpeech("Sorry I cannot find the weather for " + city);
    else:
        main = responseJson["main"];
        wind = responseJson["wind"];
        weather = responseJson["weather"];
        temperature = str(int(main["temp"]));
        airPressure = str(int(main["pressure"]));
        humidity = str(int(main["humidity"]));
        windSpeed = str(int(wind["speed"]));
        description = weather[0]["description"];
        textToSpeech("The current temperature in " + city + " is " + temperature + " degrees, the current air pressure is " + airPressure + ", the current humidity is " + humidity + ", the current wind speed is " + windSpeed + " miles per hour. The weather looks like it is " + description);

def temperature(textToSpeech, phrases, text):
    textString = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) and "" or " ");

    city = "";

    for phrase in phrases["now"]:
        city = textString.split("in")[1].replace(phrase, "");
    
    weatherResponse = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=8113fec12b95b254d44c72b30f271319&q=" + city + "&units=imperial");
    responseJson = weatherResponse.json();
    responseCode = responseJson["cod"];
    
    if (responseCode == "404"):
        textToSpeech("Sorry I cannot find the temperature for " + city);
    else:
        main = responseJson["main"];
        temperature = str(int(main["temp"]));
        textToSpeech("The current temperature in " + city + " is " + temperature + " degrees,");

def airPressure(textToSpeech, phrases, text):
    textString = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) and "" or " ");

    city = "";

    for phrase in phrases["now"]:
        city = textString.split("in")[1].replace(phrase, "");

    weatherResponse = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=8113fec12b95b254d44c72b30f271319&q=" + city + "&units=imperial");
    responseCode = responseJson["cod"];

    if (responseCode == "404"):
        textToSpeech("Sorry I cannot find the air pressure for " + city);
    else:
        responseJson = weatherResponse.json();
        main = responseJson["main"];
        airPressure = str(int(main["pressure"]));
        textToSpeech("The current air pressure in " + city + " is " + airPressure);

def humidity(textToSpeech, phrases, text):
    textString = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) and "" or " ");

    city = "";

    for phrase in phrases["now"]:
        city = textString.split("in")[1].replace(phrase, "");

    weatherResponse = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=8113fec12b95b254d44c72b30f271319&q=" + city + "&units=imperial");
    responseJson = weatherResponse.json();
    responseCode = responseJson["cod"];

    if (responseCode == "404"):
        textToSpeech("Sorry I cannot find the humidity for " + city);
    else:   
        main = responseJson["main"];
        humidity = str(int(main["humidity"]));
        textToSpeech("The current humidity in " + city + " is " + humidity);

def windSpeed(textToSpeech, phrases, text):
    textString = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) and "" or " ");

    city = "";

    for phrase in phrases["now"]:
        city = textString.split("in")[1].replace(phrase, "");

    weatherResponse = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=8113fec12b95b254d44c72b30f271319&q=" + city + "&units=imperial");
    responseJson = weatherResponse.json();
    responseCode = responseJson["cod"];
    
    if (responseCode == "404"):
        textToSpeech("Sorry I cannot find the wind speed for " + city);
    else:
        wind = responseJson["wind"];
        windSpeed = str(int(wind["speed"]));
        textToSpeech("The current wind speed in " + city + " is " + windSpeed + " miles per hour");