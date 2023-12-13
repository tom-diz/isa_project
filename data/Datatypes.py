from utils.Binary import Binary

class Register:
    def __init__(self, name:str, value:int):
        '''
        The following function initializes the register.
        '''
        self.name = name
        self.value = value

    def __str__(self) -> str:
        '''
        The following function returns the string representation of the register.
        '''
        return f"{self.value}"

class Variable:
    def __init__(self, name:str, value:int):
        '''
        The following function initializes the variable.
        '''
        self.name = name
        self.value = value

    def __str__(self) -> str:
        '''
        The following function returns the string representation of the variable.
        '''
        return f"{self.value}"
    
class Constant:
    def __init__(self, value:int):
        '''
        The following function initializes the constant.
        '''
        self.name = value
        self.value = value

    def __str__(self) -> str:
        '''
        The following function returns the string representation of the constant.
        '''
        return f"{self.value}"

class Stack:
    # Binary stack: store 11 bit values
    def __init__(self):
        '''
        The following function initializes the stack.
        '''
        self.stack: list[str] = []
    
    def push(self, value:Binary) -> None:
        '''
        The following function pushes a value to the stack, with the good amount of zeros.
        '''
        self.stack.append(value.zfill(11))
    
    def pop(self) -> Binary:
        '''
        The following function pops a value from the stack.
        '''
        try:
            return Binary(self.stack.pop())
        except IndexError:
            raise Exception("Stack is empty.")
    
    def __str__(self) -> str:
        '''
        The following function returns the string representation of the stack.
        '''
        return str(self.stack)
    
    def __len__(self) -> int:
        '''
        The following function returns the length of the stack.
        '''
        return len(self.stack)