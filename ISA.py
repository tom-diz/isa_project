from utils.Memory import VariableMemory, RegisterMemory
from utils.ASM import ASM
from data.Datatypes import Stack

class ISA:
    def __init__(self):
        self.registers: RegisterMemory = RegisterMemory()
        self.memory: VariableMemory = VariableMemory()
        self.stack: Stack = Stack()
        self.r = ASM()

        self.memory.addVars(self.r.readData())
        self.registers.setRegister('T0', 0)
        self.registers.setRegister('T1', 0)
        self.registers.setRegister('T2', 0)
        self.registers.setRegister('T3', 0)

        # If LABEL isn't found, it will be added to memory
        try:
            self.memory.getDataByName('$LABEL')
        except Exception:
            self.memory.addVar('$LABEL', 999)

    
    def writeInstructions(self) -> None:
        self.r.writeBinaryInstructions(self.registers, self.memory)

    def decodeInstructions(self) -> None:
        self.r.decodeBinaryInstructions(self.registers, self.memory, self.stack)
    
    def executeInstructions(self, step:bool=True) -> None:
        self.r.computeInstructions(self.registers, self.memory, self.stack, step=step)


def execute(step:bool):
    # Class initialization
    i = ISA()

    # Write instructions
    i.writeInstructions()

    # Decode binary instructions to text
    i.decodeInstructions()

    # Execute instructions
    i.executeInstructions(step=step)