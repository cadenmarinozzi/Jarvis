import wolframalpha, json

file = open("configuration.json");
fileContents = file.read();
configuration = json.loads(fileContents);
wolfram_api_key = configuration["wolfram_alpha"]["api_key"];
client = wolframalpha.Client(wolfram_api_key);

def wolfram(textToSpeech, phrases, text):
    textString = "";

    for index, string in enumerate(text):
        textString += string + (index == len(text) - 1 and "" or " ");

    question = textString.replace("wolfram", "");

    for prefix in phrases["prefixes"]:
        question = question.replace(prefix, "");

    res = client.query(question);

    if (len(list(res.results)) > 0):
        answer = list(res.results)[0].text;
        textToSpeech(answer);