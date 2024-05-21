from microbit import *
import radio
from Message import Message
from Register import Register

registerList = [
    Register("MDR"),
    Register("MAR"),
    Register("PC"),
    Register("MBR"),
    Register("SP"),
    Register("LV"),
    Register("CPP"),
    Register("TOS"),
    Register("OPC"),
    Register("H"),
]

registers = {}
for register in registerList:
    registers[register.name.lower()] = register

while True:
    receivedMessage = radio.receive()
    if receivedMessage:
        message = Message.parseMessage(receivedMessage)
        if message and message.receiver in registers and message.value == None:
            message = Message(message.receiver, "alu", registers[message.receiver].value)
            radio.send(message.serialize())
        elif message and message.receiver in registers:
            registers[message.receiver].value = message.value
            display.scroll(registers[message.receiver].text, delay=100, wait=False, loop=True)
        else: # not relevant, message can be discarded
            pass
    
