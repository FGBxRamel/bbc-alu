class CPUEnum():
    """A class for bitflagging the CPU commands."""
    def __init__(self):
        pass
    
    @property
    def AND(self):
        return 1

    @property
    def OR(self):
        return 2

    @property
    def NEG(self):
        return 4

    @property
    def ADD(self):
        return 8

    @property
    def ENA(self):
        return 16

    @property
    def ENB(self):
        return 32

    @property
    def INV(self):
        return 64

    @property
    def INC(self):
        return 128

    @property
    def SLL8(self):
        return 256

    @property
    def SRA1(self):
        return 512

class BBusEnum():
    def __init__(self):
        pass

    @property
    def MDR(self):
        return 1

    @property
    def PC(self):
        return 2

    @property
    def MBR(self):
        return 4

    @property
    def MBRU(self):
        return 8

    @property
    def SP(self):
        return 16

    @property
    def LV(self):
        return 32

    @property
    def CPP(self):
        return 64

    @property
    def TOS(self):
        return 128

    @property
    def OPC(self):
        return 256

class CBusEnum():
    def __init__(self):
        pass
    
    @property
    def MDR(self):
        return 1

    @property
    def PC(self):
        return 2

    @property
    def MAR(self):
        return 4

    @property
    def H(self):
        return 8
    
    @property
    def SP(self):
        return 16

    @property
    def LV(self):
        return 32

    @property
    def CPP(self):
        return 64

    @property
    def TOS(self):
        return 128

    @property
    def OPC(self):
        return 256