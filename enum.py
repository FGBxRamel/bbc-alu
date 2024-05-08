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

    @property
    def ALL(self):
        return (self.ADD | self.AND | self.ENA |
            self.ENB | self.INC | self.INV |
            self.NEG | self.OR | self.SLL8 |
            self.SRA1)

class BBusEnum():
    """A class for bitflagging the BBus input."""
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

    @property
    def ALL(self):
        return (self.CPP | self.LV | self.MBR |
               self.MBRU | self.MDR | self.OPC |
               self.PC | self.SP | self.TOS)

class CBusEnum():
    """A class for bitflagging the CBus output."""
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

    @property
    def ALL(self):
        return (self.CPP | self.H | self.LV |
               self.MAR | self.MDR | self.OPC |
               self.PC | self.SP | self.TOS)