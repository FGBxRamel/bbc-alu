class Message:
    def __init__(self, sender, receiver, value = None):
        # value = None wenn Wert verlangt werden soll 
        self.sender = sender
        self.receiver = receiver
        self.value = value

    def serialize(self):
        value = "null"
        if self.value != None:
            value = hex(self.value).replace("0x", "")
        return self.sender + "," + self.receiver + "," + value

    @staticmethod
    def parseMessage(message):
        messageList = message.split(",")
        value = None
        if messageList != "null":
            value = int(messageList[2], 16)
        return Message(messageList[0], messageList[1], value)