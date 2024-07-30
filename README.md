# bbc-alu
An ALU with registers with BBC Microbits.


## Serial Communication
The oktopus machine (OM) never reads from the serial.
The OM sends two types of messages over serial to coms:
### A: command to Alu
OM sends command addressed to alu in the following format:
```
"ALU#<H>#<B>#<COMMAND>\r\n"
```
the message is seperated by '#' and ends with "\r\n"
\<H\> is "H" if the current micro command has "ena" set, else is "0" *
\<B\> the name of the register to be put on the bbus if the current micro command has "enb" set, else is "0" *
\<COMMAND\> can be "&", "|", "-", or "+"

coms sends the message to alu in the following format:
```
"coms,alu,<H>#<B>#<COMMAND>"
```
#### Example
```
OM sends "ALU#H#MDR+\r\n" to coms over serial
  -> coms sends "coms,alu,H#MDR#+" over radio
OM sends "ALU#0#0+\r\n" to coms over serial
  -> coms sends "coms,alu,0#0#+" over radio
```

### B: OM sends value addressed to register
OM sends a value addressed directly to a register to be saved
The message has the following format:
```
"<register>#<value>\r\n"
```
\<register\> is the name of the register in which the value is to be saved
\<value\> is the value which is to be saved

coms sends the message to the register in the following format:
```
"coms,<register>,<value>"
```
#### Example
```
OM sends "MDR#0x89b\r\n" to coms over serial
  -> coms sends "coms,mdr,0x89b" over radio
OM sends "MBR#0x45c\r\n" to coms over serial
  -> coms sends "coms,mbr,0x45c" over radio
```




*I think. Sure hope this is how this works. Honestly, I have no idea wtf is going on in the oktopus machine and trying to understand it hurts my tiny, smooth brain, so it could be entirely possible that what I wrote here is incorrect.
