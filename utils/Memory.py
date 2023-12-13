from typing import Dict
from data.Datatypes import Variable

class VariableMemory:
    # Memory structure: (binary address, (name, value))
    def __init__(self):
        self.memory: Dict[int, Variable] = {}
    
    def addData(self, address:int, name:str, value:int) -> None:
        self.memory[address] = Variable(name, value)
    
    def addVars(self, data:list[dict[str, int]]) -> None:
        for var in data:
            for name in var:
                self.addData(self.findFreeAddress(), name, var[name]) 
    
    def addVar(self, name:str, value:int) -> None:
        self.addData(self.findFreeAddress(), name, value)

    def findFreeAddress(self) -> int:
        # Start searching from address 0
        address = 0
        while address in self.memory:
            address += 1
        return address 
    
    def getData(self, address:int) -> Variable:
        return self.memory[address]
    
    def getDataByName(self, name:str) -> Variable:
        for address in self.memory:
            if self.memory[address].name == name:
                return self.memory[address]
        raise Exception("Variable not found.")
    
    def getDataAddressByName(self, name:str) -> int:
        for address in self.memory:
            if self.memory[address].name == name:
                return address
        raise Exception("Variable not found.")

    def getVariableByAddress(self, address:int) -> Variable:
        return self.memory[address]
    
    def setDataByName(self, name:str, value:int) -> None:
        for address in self.memory:
            if self.memory[address].name == name:
                self.memory[address].value = value
                return
        raise Exception("Variable not found.")
    
    def setDataByAddress(self, address:int, value:int) -> None:
        if address in self.memory:
            self.memory[address].value = value
            return

        else:
            raise Exception("Variable not found.")
class RegisterMemory:
    def __init__(self):
        self.memory: Dict[str, int] = {'T0': 0, 'T1': 0, 'T2': 0, 'T3': 0}
    
    def getRegister(self, name:str) -> int:
        return self.memory[name]
    
    def getRegisterNumber(self, name:str) -> int:
        return int(name[1])
    
    def setRegister(self, name:str, value:int) -> None:
        self.memory[name] = value