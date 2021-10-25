import speedtest

speedTest = speedtest.Speedtest();

def download(textToSpeech, phrases, text, server):
    downloadSpeed = speedTest.download();
    formattedDownloadSpeed = int(downloadSpeed * 9.537 * 10 ** -7);
    speechString = "The current download speed is " + str(formattedDownloadSpeed) + " megabytes per second";
    textToSpeech(speechString);

def upload(textToSpeech, phrases, text, server):
    uploadSpeed = speedTest.upload();
    formattedUploadSpeed = int(uploadSpeed * 9.537 * 10 ** -7);
    speechString = "The current upload speed is " + str(formattedUploadSpeed) + " megabytes per second"
    textToSpeech(speechstring);