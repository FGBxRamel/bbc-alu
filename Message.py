class Message:
    def __init__(self, receiver, sender, value = None):
        # value = None wenn Wert verlangt werden soll 
        self.receiver = receiver
        self.sender = sender
        self.value = value

    def serialize(self):
        value = "null"
        if self.value != None:
            value = hex(self.value).replace("0x", "")
        return self.sender + "," + self.receiver + "," + value

    @staticmethod
    def parseMessage(message):
        try:
            messageList = message.split(",")
            value = None
            if messageList[2] != "null":
                value = int(messageList[2], 16)
            return Message(messageList[0], messageList[1], value)
        except:
            return False
