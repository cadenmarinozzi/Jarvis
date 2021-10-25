import wolframalpha, json

file = open("configuration.json");
fileContents = file.read();
configuration = json.loads(fileContents);
wolfram_api_key = configuration["wolframAlpha"]["apiKey"];
client = wolframalpha.Client(wolfram_api_key);

def wolfram(textToSpeech, phrases, text, server):
    textString = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) - 1 and "" or " ");

    question = textString.replace("wolfram", "");

    for prefix in phrases["prefixes"]:
        question = question.replace(prefix, "");

    response = client.query(question);

    if (len(list(response.results)) > 0):
        answer = list(response.results)[0].text;
        textToSpeech(answer);