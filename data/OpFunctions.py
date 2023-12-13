from data.Datatypes import Variable, Register, Constant, Stack
from utils.Memory import VariableMemory, RegisterMemory
from utils.Binary import Binary

class OpFunctions:

    @staticmethod
    def LDA(a:Register, b:Register|Variable|Constant, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### LDA <reg1> <reg2>/<var>/<const> - OP Code 00000
        Load register reg1 with the contents of either the contents of reg2, or the memory var or a constant 
        const. Memory regions loads (load into a variable, for instance) are NOT ALLOWED.
        '''

        reg.setRegister(a.name, b.value)

        return counter

    @staticmethod
    def STR(a:Variable, b:Register|Constant, var:VariableMemory, reg:None, stack:None, counter:int) -> int:
        '''
        ### STR <var> <reg>/<const> - OP Code 00001
        Store in the memory position referred by var the value of register reg or a constant const. Register 
        stores (store into register t0, for instance) are NOT ALLOWED.
        '''
        # a.value -> Index of the array
        # b.value -> Value to be stored

        var.setDataByName(a.name, b.value)

        return counter

    @staticmethod
    def PUSH(a:Register|Variable|Constant, b:None, var:VariableMemory, reg:None, stack:Stack, counter:int) -> int:
        '''
        ### PUSH <reg>/<var>/<const> - OP Code 00010
        Push to the top of the stack the contents of reg or var or a constant const.
        '''

        stack.push(Binary(a.value))
        
        return counter

    @staticmethod
    def POP(a:Register, b:None, var:None, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### POP <reg> - OP Code 00000
        Pop from the top of the stack and store the value on reg. Storing in a memory region is NOT ALLOWED.
        '''

        reg.setRegister(a.name, stack.pop().__INT__())
        
        return counter

    @staticmethod
    def AND(a:Register, b:Register|Variable|Constant, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### AND <reg1> <reg2>/<var>/<const> - OP Code 00011
        Performs a logical AND operation between reg1 and a register reg2, a variable var or a constant 
        const, and store the result on register reg1. Memory regions stores (store result into a variable, for 
        instance) are NOT ALLOWED.
        '''
        
        a_reg = Binary(a.value)

        b_val = Binary(b.value)

        a_reg.__AND__(b_val)

        print(a_reg.__INT__())
        
        reg.setRegister(a.name, a_reg.__INT__())

        return counter

    @staticmethod
    def OR(a:Register, b:Register|Variable|Constant, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### OR <reg1> <reg2>/<var>/<const> - OP Code 00100
        Performs a logical OR operation between reg1 and a register reg2, a variable var or a constant 
        const, and store the result on register reg1. Memory regions stores (store result into a variable, for 
        instance) are NOT ALLOWED.
        '''

        a_reg = Binary(a.value)

        b_val = Binary(b.value)

        a_reg.__OR__(b_val)

        reg.setRegister(a.name, a_reg.__INT__())
        
        return counter

    @staticmethod
    def NOT(a:Register, b:None, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### NOT <reg> - OP Code 00000
        Performs a logical NOT operation on register reg and store the result on register reg. Memory 
        regions stores (store result into a variable, for instance) are NOT ALLOWED.
        '''

        a_reg = Binary(a.value)

        a_reg.__NOT__()

        reg.setRegister(a.name, a_reg.__INT__())
        
        return counter

    @staticmethod
    def ADD(a:Register, b:Register|Variable|Constant, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### ADD <reg1> <reg2>/<var>/<const> - OP Code 00101
        Performs the addition operation of reg1 and a register reg2, a variable var or a constant const, and 
        store the result on register reg1. Memory regions stores (store result into a variable, for instance) 
        are NOT ALLOWED.
        '''

        reg.setRegister(a.name, b.value + a.value)

        return counter

    @staticmethod
    def SUB(a:Register, b:Register|Variable|Constant, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### SUB <reg1> <reg2>/<var>/<const> - OP Code 00110
        Performs the subtraction operation of reg1 and a register reg2, a variable var or a constant const, 
        and store the result on register reg1. The operation is given by second argument minus the first 
        argument (i.e., reg2 – reg1). Memory regions stores (store result into a variable, for instance) are 
        NOT ALLOWED.
        '''

        reg.setRegister(a.name, b.value - a.value)

        return counter

    @staticmethod
    def DIV(a:Register, b:Register|Variable|Constant, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### DIV <reg1> <reg2>/<var>/<const> - OP Code 00111
        Performs the integer division operation of reg1 and a register reg2, a variable var or a constant 
        const, and store the result on register reg1. The operation is given by second argument divided by
        the first argument (i.e., reg2 / reg1). Memory regions stores (store result into a variable, for 
        instance) are NOT ALLOWED.
        '''

        reg.setRegister(a.name, int(b.value / a.value))
        
        return counter

    @staticmethod
    def MUL(a:Register, b:Register|Variable|Constant, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### MUL <reg1> <reg2>/<var>/<const> - OP Code 01000
        Performs the integer multiplication operation of reg1 and a register reg2, a variable var or a 
        constant const, and store the result on register reg1. Memory regions stores (store result into a 
        variable, for instance) are NOT ALLOWED.
        '''
        
        reg.setRegister(a.name, b.value * a.value)
        
        return counter

    @staticmethod
    def MOD(a:Register, b:Register|Variable|Constant, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### MOD <reg1> <reg2>/<var>/<const> - OP Code 01001
        Performs the integer modulo operation of reg1 and a register reg2, a variable var or a constant 
        const, and store the result on register reg1. The operation is given by second argument modulo the 
        first argument (i.e., reg2 mod reg1). Memory regions stores (store result into a variable, for 
        instance) are NOT ALLOWED.
        '''

        reg.setRegister(a.name, b.value % a.value)
        
        return counter

    @staticmethod
    def INC(a:Register, b:None, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:

        '''
        ### INC <reg> - OP Code 01010
        Increments the value of a register reg. Memory increments (incrementing a variable, for instance) 
        are NOT ALLOWED.
        '''

        reg.setRegister(a.name, a.value + 1)
        
        return counter

    @staticmethod
    def DEC(a:Register, b:None, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### DEC <reg> - OP Code 01011
        Decrements the value of a register reg. Memory increments (decrementing a variable, for instance) 
        are NOT ALLOWED.
        '''

        reg.setRegister(a.name, a.value - 1)

        return counter

    @staticmethod
    def BEQ(a:Register|Variable|Constant, b:Register|Variable|Constant, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### BEQ <reg1>/<var1>/<const1> <reg2>/<var2>/<const2> <LABEL> - OP Code 01100
        Performs a comparison between two values, given by registers, variables or constants. Any 
        combination is permitted. If they are equal, jump to the address defined by the label LABEL
        '''

        if a.value == b.value:
            return var.getDataByName('$LABEL').value
        
        return counter

    @staticmethod
    def BNE(a:Register|Variable|Constant, b:Register|Variable|Constant, var:VariableMemory, reg:None, stack:Stack, counter:int) -> int:
        '''
        ### BNE <reg1>/<var1>/<const1> <reg2>/<var2>/<const2> <LABEL> - OP Code 01101
        Performs a comparison between two values, given by registers, variables or constants. Any 
        combination is permitted. If they are different, jump to the address defined by the label LABEL
        '''

        if a.value != b.value:
            return var.getDataByName('$LABEL').value
        
        return counter

    @staticmethod
    def BBG(a:Register|Variable|Constant, b:Register|Variable|Constant, var:VariableMemory, reg:None, stack:Stack, counter:int) -> int:
        '''
        ### BBG <reg1>/<var1>/<const1> <reg2>/<var2>/<const2> <LABEL> - OP Code 01110
        Performs a comparison between two values, given by registers, variables or constants. Any 
        combination is permitted. If the first parameter is bigger than the second parameter, jump to the 
        address defined by the label LABEL
        '''

        if a.value > b.value:
            return var.getDataByName('$LABEL').value
        
        return counter

    @staticmethod
    def BSM(a:Register|Variable|Constant, b:Register|Variable|Constant, var:VariableMemory, reg:None, stack:Stack, counter:int) -> int:
        '''
        ### BSM <reg1>/<var1>/<const1> <reg2>/<var2>/<const2> <LABEL> - OP Code 01111
        Performs a comparison between two values, given by registers, variables or constants. Any 
        combination is permitted. If the first parameter is smaller than the second parameter, jump to the 
        address defined by the label LABEL
        '''

        if a.value < b.value:
            return var.getDataByName('$LABEL').value
        
        return counter

    @staticmethod
    def JMP(a:Variable, b:None, var:VariableMemory, reg:None, stack:Stack, counter:int) -> int:
        '''
        ### JMP <LABEL> - OP Code 10000
        Jump to the address defined by the label LABEL
        '''

        return a.value

    @staticmethod
    def HLT(a:Register|Variable|Constant, b:Register|Variable|Constant, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### HLT - OP Code 10001
        End the program execution.
        '''

        return -1
    
    @staticmethod
    def LOAD(a:Variable, b:Register|Variable|Constant, var:VariableMemory, reg:RegisterMemory, stack:Stack, counter:int) -> int:
        '''
        ### LOAD <var> <var>/<reg>/<const> - OP Code 10010
        Load the value of a var, reg or const into a variable var.
        '''
    
        var.setDataByName(a.name, b.value)

        return counter
