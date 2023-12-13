from enum import Enum

class OpType(Enum):
    REGISTER = 0b00
    VARIABLE = 0b01
    CONSTANT = 0b10

class OpCode(Enum):
    # (opcode, (arg1 type, arg2 types))
    LDA = (0b00000, ([OpType.REGISTER], [OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT]))
    STR = (0b00001, ([OpType.VARIABLE], [OpType.REGISTER, OpType.CONSTANT]))
    PUSH = (0b00010, ([OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT], None))
    POP = (0b00011, ([OpType.REGISTER], None))
    AND = (0b00100, (OpType.REGISTER, [OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT]))
    OR = (0b00101, (OpType.REGISTER, [OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT]))
    NOT = (0b00110, ([OpType.REGISTER], None))
    ADD = (0b00111, (OpType.REGISTER, [OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT]))
    SUB = (0b01000, (OpType.REGISTER, [OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT]))
    DIV = (0b01001, (OpType.REGISTER, [OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT]))
    MUL = (0b01010, (OpType.REGISTER, [OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT]))
    MOD = (0b01011, (OpType.REGISTER, [OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT]))
    INC = (0b01100, ([OpType.REGISTER], None))
    DEC = (0b01101, ([OpType.REGISTER], None))
    BEQ = (0b01110, (OpType.REGISTER, [OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT,
                                     OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT]))
    BNE = (0b01111, (OpType.REGISTER, [OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT,
                                     OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT]))
    BBG = (0b10000, (OpType.REGISTER, [OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT,
                                      OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT]))
    BSM = (0b10001, (OpType.REGISTER, [OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT,
                                      OpType.REGISTER, OpType.VARIABLE, OpType.CONSTANT]))
    JMP = (0b10010, ([OpType.VARIABLE], None))
    HLT = (0b10011, None)
    LOAD = (0b10100, None)

class OpRegister(Enum):
    T0 = 0b0000
    T1 = 0b0001
    T2 = 0b0010
    T3 = 0b0011

def getParameterType(parameter:str) -> OpType:
    if (parameter[0] == "T" and parameter[1] in ["0", "1", "2", "3"]) or parameter == "LABEL":
        return OpType.REGISTER
    elif parameter[0] == "$":
        return OpType.VARIABLE
    elif parameter.isnumeric():
        return OpType.CONSTANT
    else:
        raise Exception("Invalid parameter type.")

def getParameterAmount(instruction:list[str]) -> int:
    return len(instruction)