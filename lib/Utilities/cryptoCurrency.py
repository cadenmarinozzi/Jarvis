from datetime import datetime
import requests

def cryptoCurrency(name):
    time = datetime.now().time().strftime("%H");
    responseData = requests.get("https://min-api.cryptocompare.com/data/price?fsym=" + name + "&tsyms=USD");
    responseJson = responseData.json();
    price = responseJson["USD"];

    return [
        price,
        int(time)
    ];