class CPUEnum:
    """A class for bitflagging the CPU commands."""
    AND = 1024
    OR = 2
    NEG = 4
    ADD = 8
    ENA = 16
    ENB = 32
    INV = 64
    INC = 128
    SLL8 = 256
    SRA1 = 512
    ALL = (ADD | AND | ENA | ENB | INC | INV | NEG | OR | SLL8 | SRA1)
    OPERATIONS = (AND | OR | NEG | ADD)


class BBusEnum:
    """A class for bitflagging the BBus input."""
    MDR = 512
    PC = 2
    MBR = 4
    MBRU = 8
    SP = 16
    LV = 32
    CPP = 64
    TOS = 128
    OPC = 256
    ALL = (CPP | LV | MBR | MBRU | MDR | OPC | PC | SP | TOS)


class CBusEnum:
    """A class for bitflagging the CBus output."""
    MDR = 512
    PC = 2
    MAR = 4
    H = 8
    SP = 16
    LV = 32
    CPP = 64
    TOS = 128
    OPC = 256
    ALL = (CPP | H | LV | MAR | MDR | OPC | PC | SP | TOS)
