# bbc-alu
An ALU with registers with BBC Microbits.


## Protocol specification
### General
Values looking like \<this\> are required, values like \[this\] are optional. All sent values are strings, the "value" coloumn therefore specifies as what it should be parsed.
### ALU - Registers
The message sent between the ALU and the registers has the following format:
```
<sender>,<recipient>,[value]
```
| Value     | Type | Description                                      | Example |
|-----------|------|--------------------------------------------------|---------|
| sender    | str  | The sender of the value.                         | alu     |
| recipient | str  | For who the message is for.                      | tos     |
| value     | hex \| "null"  | The hex value that should be saved or is sent, without "0x". "null" when there is no value specified or the register is empty. | 89b     |

If the ALU sends a message with "null" as value it requests the value of that register. If a value is specified, the register should save it. A register can only send "null" when it is empty, otherwise it sends its value if requested.  
#### Example
```
alu,tos - Alu wants value of TOS
tos,alu,0x89b - TOS sends value "0x89b" to ALU
alu,mdr,0x45c - ALU sends value "0x45c" to write to MDR
```