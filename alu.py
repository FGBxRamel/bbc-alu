from enums import *
import radio
from time import sleep

cpuEnum, bbusEnum, cbusEnum = CPUEnum(), BBusEnum(), CBusEnum()


class Alu():
    """The Aritmetic Logic Unit takes commands and processes them."""

    def __init__(self):
        radio.config()

    def start(self):
        """Starts the ALU."""
        while True:
            message = None
            while message is None:
                sleep(0.05)
                message = radio.receive()
            cpuFlag, bbusFlag, cbusFlag = 0, 0, 0
            # NOTE Wait for comms team to see what we get
            # Asssume that we have a bitflag for the ports

            # If we don't put the output somewhere we can just stop
            if cbusFlag & cbusEnum.ALL == 0:
                continue

            # NOTE Have to wait for comms to see what the function gets
            bbusData = self._getRegister(0) if (
                cpuFlag & cpuEnum.ENB) != 0 else 0
            abusData = self._getRegister(0) if (
                cpuFlag & cpuEnum.ENA) != 0 else 0

            cbusData = self._processCPU(cpuFlag, abusData, bbusData)
            # TODO Send the data to the registers specified in cbusFlag

    def _parseCommand(self, rawCommand):
        """\
        Parses whatever it gets into three flags and returns them.
        Order: cpu, bbus, cbus.
        """
        cpuFlag, bbusFlag, cbusFlag = 0, 0, 0
        # TODO Wait for comms
        return cpuFlag, bbusFlag, cbusFlag

    def _processCPU(self, cpuFlag, abusData, bbusData):
        """Processes the CPU flag and returns the output (cbusData)."""
        cbusData = 0
        # Make the operation
        cpuOperation = cpuFlag & cpuEnum.OPERATIONS
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
        # TODO See what INV operation does and implement it
        if (cpuFlag & cpuEnum.INC) == cpuEnum.INC:
            cbusData += 1

        # Check the shifts
        if (cpuFlag & cpuEnum.SLL8) == cpuEnum.SLL8:
            cbusData << 8
        elif (cpuFlag & cpuEnum.SRA1) == cpuEnum.SRA1:
            cbusData >> 1

        return cbusData

    def _getRegister(self, register):
        """Gets the data that a specified register holds."""
        # TODO Wait for comms
        pass

    def _setRegister(self, register, data):
        """Puts data into a specified register."""
        # TODO Wait for comms
        pass
