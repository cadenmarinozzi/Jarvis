import speedtest

speedTest = speedtest.Speedtest();

def download(textToSpeech, phrases, text):
    downloadSpeed = speedTest.download();
    formattedDownloadSpeed = int(downloadSpeed * 9.537 * 10 ** -7);
    textToSpeech("The current download speed is " + str(formattedDownloadSpeed) + " megabytes per second");

def upload(textToSpeech, phrases, text):
    uploadSpeed = speedTest.upload();
    formattedUploadSpeed = int(uploadSpeed * 9.537 * 10 ** -7);
    textToSpeech("The current upload speed is " + str(formattedUploadSpeed) + " megabytes per second");