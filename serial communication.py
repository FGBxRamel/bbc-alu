from microbit import *
import radio

radio.on()
# serial communication
uart.init()

# list of valid registers
registers = ["mdr", "pc", "mbr", "mbru", "sp", "lv", "cpp", "tos", "opc", "0"]
# list of valid commands
commands = ["&", "|", "-", "+"]

while True:
    receivedMessage = None
    if uart.any():
        receivedMessage = str(uart.readline())
        # uart.readline() returns the newline at the end, so we shave that off
        receivedMessage.strip()
        receivedMessage.split('#')

        # if valid message addressed to alu
        if receivedMessage[0] == "ALU" and receivedMessage[2] in registers and receivedMessage[3] in commands:
            radio.send("coms," + "alu," + receivedMessage[1] + "#" + receivedMessage[2] + "#" + receivedMessage[3])

        # else if addressed to register directly
        elif receivedMessage[0].lower() in registers:
            radio.send("coms," + receivedMessage[0] + "," + receivedMessage[1])

        # else do nothing and await/read next message
