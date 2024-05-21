from enums import *
import radio
from time import sleep

cpuEnum, bbusEnum, cbusEnum = CPUEnum(), BBusEnum(), CBusEnum()


class Alu():
    """The Aritmetic Logic Unit takes commands and processes them."""

    def __init__(self):
        radio.config()

    @staticmethod
    def _parseCommand(rawCommand: str) -> int:
        """\
        Parses whatever it gets into three flags and returns them.
        Order: cpu, bbus, cbus.
        """
        # NOTE This assumes it gets the flags as a csv seperated string
        cpuFlag, bbusFlag, cbusFlag = rawCommand.split(",")
        return int(cpuFlag), int(bbusFlag), int(cbusFlag)

    def start(self) -> None:
        """Starts the ALU."""
        while True:
            message = None
            while message is None:
                sleep(0.05)
                message = radio.receive()
            # NOTE Wait for comms team to see what we *actually* get
            cpuFlag, bbusFlag, cbusFlag = self._parseCommand(message)

            # If we don't put the output somewhere we can just stop
            if cbusFlag & cbusEnum.ALL == 0:
                continue

            bbusRegister = self._getRegisterString(bbusFlag)

            bbusData = self._getRegister(bbusRegister) if (
                cpuFlag & cpuEnum.ENB) else 0
            abusData = self._getRegister() if (
                cpuFlag & cpuEnum.ENA) else 0

            cbusData = self._processCPU(cpuFlag, abusData, bbusData)
            cbusRegister = self._getRegisterString(cbusFlag)
            self._setRegisters()

    def _processCPU(self, cpuFlag: int, abusData: int, bbusData: int) -> int:
        """Processes the CPU flag and returns the output (cbusData)."""
        cbusData: int = 0
        # Check for invert
        if (cpuFlag & cpuEnum.ENA) and (cpuFlag & cpuEnum.INV):
            abusData = ~abusData

        # Make the operation
        cpuOperation: int = cpuFlag & cpuEnum.OPERATIONS
        if cpuOperation % 2 != 0 or cpuOperation == 0:
            print("Multiple or no CPU Operation given, assuming ADD.")
            cpuOperation = cpuEnum.ADD

        if cpuFlag == cpuEnum.AND:
            cbusData = abusData & bbusData
        elif cpuFlag == cpuEnum.OR:
            cbusData = abusData | bbusData
        elif cpuFlag == cpuEnum.NEG:
            cbusData = -bbusData
        elif cpuFlag == cpuEnum.ADD:
            cbusData = bbusData + abusData

        # Check the other CPU Flags

        if (cpuFlag & cpuEnum.INC):
            cbusData += 1

        # Check the shifts
        if (cpuFlag & cpuEnum.SLL8) == cpuEnum.SLL8:
            cbusData << 8
        elif (cpuFlag & cpuEnum.SRA1) == cpuEnum.SRA1:
            cbusData >> 1

        return cbusData

    def _getRegister(self, register: str) -> int:
        """Gets the data that a specified register holds. Returns 0 if no data is returned."""
        message: str = "alu," + register + ",null"
        radio.send(message)
        returned_message: str = None
        while returned_message is None:
            sleep(0.05)
            returned_message = radio.receive()
        returned_value = returned_message.split(",")[2]
        return 0 if returned_value == "null" else int(returned_value, 16)

    def _setRegisters(self, registers: int, data: int):
        """Puts data into a specified register."""
        data: str = hex(data)[2:]
        register = self._getRegisterString(registers)
        message: str = "alu," + register + "," + data
        radio.send(message)

    def _getRegisterString(self, register: int) -> str:
        register_name = None
        if register & (BBusEnum.MDR | CBusEnum.MDR):
            register_name = "mdr"
        elif register & (BBusEnum.PC | CBusEnum.PC):
            register_name = "pc"
        elif register & BBusEnum.MBR:
            register_name = "mbr"
        elif register & BBusEnum.MBR:
            register_name = "mbru"
        elif register & (BBusEnum.SP | CBusEnum.SP):
            register_name = "sp"
        elif register & (BBusEnum.LV | CBusEnum.LV):
            register_name = "lv"
        elif register & (BBusEnum.CPP | cbusEnum.CPP):
            register_name = "cpp"
        elif register & (BBusEnum.OPC | CBusEnum.OPC):
            register_name = "opc"
        elif register & (BBusEnum.TOS | CBusEnum.TOS):
            register_name = "tos"
        elif register & CBusEnum.MAR:
            register_name = "mar"
        elif register & CBusEnum.H:
            register_name = "h"
        return register_name
