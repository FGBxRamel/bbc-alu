from microbit import *
import radio
from Message import Message
from Register import Register

registerList = [
    Register("MDR", 0),
    Register("MAR", 1),
    Register("PC", 22),
    Register("MBR", 14),
    Register("SP"),
    Register("LV"),
    Register("CPP"),
    Register("TOS"),
    Register("OPC"),
    Register("H"),
]

registers = {}
for register in registers:
    registers[register.name] = register

currentIndex = 0

while True:
    receivedMessage = radio.receive()
    if receivedMessage:
        message = Message.parseMessage(receivedMessage)
        if message.value == None:
            pass
    if button_a.was_pressed():
        currentIndex = (currentIndex + 1) % len(registerList)
    if button_b.was_pressed():
        currentIndex = 0;
    display.scroll(registerList[currentIndex].text, delay=30)