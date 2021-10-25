import psutil, math

def cpu(textToSpeech, phrases, text, server):
    usage = psutil.cpu_percent();
    formattedUsage = str(math.floor(usage));
    speechString = "The current c.p.u usage is " + formattedUsage + "%";
    textToSpeech(speechString);

def ram(textToSpeech, phrases, text, server):
    used = psutil.virtual_memory().used;
    i = int(math.floor(math.log(used, 1024)));
    sizeBytes = math.floor(used);
    usage = (sizeBytes == 0 and "0B" or "%s %s" % (round(sizeBytes / math.pow(1024, i), 2), ("Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes")[i]));
    speechString = "The current ram usage is " + usage;
    textToSpeech("The current ram usage is " + usage);