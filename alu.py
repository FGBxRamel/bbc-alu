from enum import CommandEnum
import radio


# NOTE "Schieberegister":
# 8 Bits nach links oder eins nach rechts schieben

class Alu():
    """The Aritmetic Logic Unit takes commands and processes them."""
    def __init__(self):
        radio.config()
        radio.on()

    def start(self):
        """Starts the ALU."""
        while True:
            message = None
            while message is None:
                sleep(0.05)
                message = radio.receive()
            # NOTE Wait for comms team to see what we get

    def _parseCommand(self, command):
        pass