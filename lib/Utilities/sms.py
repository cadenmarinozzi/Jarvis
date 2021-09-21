class SMS():
    def __init__(self, client):
        self.client = client;

    def send(self, sender, receiver, message):
        sent = self.client.messages.create(to = receiver, from_ = sender, body = message);

        return sent;

    def receive(self, receiver):
        returnMessages = [];
        messages = self.client.messages.list(to = receiver);

        for message in messages:
            returnMessages.append(message);

        return returnMessages;