# Read data inside instructions.txt and store the data in a list corresponding to each category
from utils.Memory import VariableMemory, RegisterMemory
from utils.Binary import Binary
from utils.Color import Color
from data.Datatypes import Register, Constant, Stack
from data.OpFunctions import OpFunctions
from data.OpCode import OpCode, OpType, OpRegister, getParameterType, getParameterAmount
from typing import get_type_hints



class ASM():
    def __init__(self, file:str = "./data/instructions/instructions.txt") -> None:
        self.ASM = open(file, "r")
        self.ASMLines = self.ASM.readlines()
        self.ASM.close()

    # readData: read until next "#" or end of file and return the data. Store the data in a list of dicts (name, value)
    def readData(self) -> list[dict[str, int]]:

        data:list[dict[str, int]] = []

        dataSector:bool = False

        for line in self.ASMLines:

            if "#" in line:
                if "DATA" in line:
                    dataSector = True
                else:
                    dataSector = False
                continue

            if dataSector:
                if line == "\n" or line == "":
                    continue
                else:
                    line = line.removesuffix("\n").split(" ")
                    data.append({line[0]: int(line[1])})
        
        return data

    # Format: [Instruction Name, Value1, Value 2...]
    def readInstructions(self) -> list[str]:
    
        # Only read the code inside the "CODE" section
        codeSector:bool = False

        instructions:list[str] = []

        for line in self.ASMLines:

            if "#" in line:
                if "CODE" in line:
                    codeSector = True
                else:
                    codeSector = False
                continue

            if codeSector:
                if line == "\n":
                    continue
                else:
                    line = line.removesuffix("\n").removesuffix(" ")

                    if (line == ''):
                        continue

                    instructions.append(line)
                
        return instructions
    
    def writeBinaryInstructions(self, registers:RegisterMemory, var_memory:VariableMemory):
        '''
        The following function translates the instructions into binary code.
        > Encoding format (32 bits):
        - Instruction type (6 bits)
        - Parameter1 Type (2 bits)
        - Parameter1 Value (11 bits)
        - Parameter2 Type (2 bits)
        - Parameter2 Value (11 bits)
        '''

        # Read the instructions
        instructions = self.readInstructions()

        # Open the binary file
        binaryFile = open("./data/instructions/binaryFile.txt", "w")
        
        # Iterate through the instructions
        for instruction in instructions:

            # Create a list to store binary values of arg1 and arg2
            argBinaryData:list[list[Binary]] = [[Binary(0), Binary(0)], [Binary(0), Binary(0)]]

            # Split the instruction into its components
            instruction = instruction.split(" ")

            # Get the instruction type
            instructionType = instruction[0]

            # Get the instruction type in binary
            try:
                instructionType = bin(OpCode[instructionType].value[0])
            except KeyError:
                raise Exception("Invalid instruction type.")

            # Get the instruction parameters
            instructionParameters = instruction[1:]

            # 3 cases:
            # - Register (T0: 00000000000, T1: 00000000001, T2: 00000000010, T3: 00000000011)
            # - Variable (String which is not a register)
            # - Constant (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10...)

            
            # Depending on the number of parameters, we will have to do different things
            parameterAmount = getParameterAmount(instructionParameters)

            if parameterAmount > 2:
                raise Exception(f"{Color.RED.value} Invalid number of parameters: {parameterAmount} parameters were given, but only 2 are allowed. {Color.RESET.value}")

            if parameterAmount > 0:
                i = 0
                for parameter in instructionParameters:
                    parameterType = getParameterType(parameter)

                    if parameterType == OpType.REGISTER:
                        argBinaryData[i][0] = Binary(0b00)
                        argBinaryData[i][1] = Binary(registers.getRegisterNumber(parameter))
                    
                    elif parameterType == OpType.VARIABLE:
                        argBinaryData[i][0] = Binary(0b01)
                        argBinaryData[i][1] = Binary(var_memory.getDataAddressByName(parameter))
                    
                    elif parameterType == OpType.CONSTANT:
                        argBinaryData[i][0] = Binary(0b10)
                        argBinaryData[i][1] = Binary(int(parameter))

                    i+=1

            # Make the binary string (with the good quantity of 0s)
            binaryString = instructionType[2:].zfill(6) + argBinaryData[0][0].zfill(2) + argBinaryData[0][1].zfill(11) + argBinaryData[1][0].zfill(2) + argBinaryData[1][1].zfill(11)

            # Write the binary string in the file
            binaryFile.write(binaryString)
    
    def decodeBinaryInstructions(self, registers: RegisterMemory, var_memory: VariableMemory, stack:Stack):
        '''
        The following function decodes the instructions binary file. The encoding format remains the same.
        > Encoding format (32 bits):
        - Instruction type (6 bits)
        - Parameter1 Type (2 bits)
        - Parameter1 Value (11 bits)
        - Parameter2 Type (2 bits)
        - Parameter2 Value (11 bits)

        It has to return the instruction name and its parameters inside a list. (e.g. [["LDA", "T0", "$var1"],...])
        '''

        # Open the binary file
        binaryFile = open("./data/instructions/binaryFile.txt", "r")

        # Read the binary file
        binaryInstructions = binaryFile.readline()

        # Split every 32 bits
        binaryInstructions = [binaryInstructions[i:i+32] for i in range(0, len(binaryInstructions), 32)]

        # Close the binary file
        binaryFile.close()

        # Open the decoded file
        decodedFile = open("./data/instructions/decodedFile.txt", "w")

        # Iterate through the binary instructions
        for binaryInstruction in binaryInstructions:

            # Remove the \n
            binaryInstruction = binaryInstruction.removesuffix("\n")

            # INSTRUCTION TYPE
            try:
                instructionOpcode = ''
                opcode_value = Binary(int(binaryInstruction[:6], 2)).zfill(5)
                # Compare the instruction type with the OpCode enum
                for opcode in OpCode:
                    if opcode.value[0] == int(opcode_value, 2):
                        instructionOpcode = opcode.name
                if instructionOpcode == '':
                    raise Exception("Invalid instruction type : the specified instruction type does not exist.")
            except ValueError:
                raise Exception("Invalid instruction type.")
                        
            # PARAMETER 1 TYPE
            try:
                # Get the parameter1 type in binary (example: 0b00)
                parameter1Type = Binary(int(binaryInstruction[6 :8], 2)).zfill(2)
                # Compare the parameter1 type with the OpType enum
                parameter1Type = OpType(int(parameter1Type, 2))
            except ValueError:
                raise Exception("Invalid parameter type.")
            
            # PARAMETER 1 VALUE
            parameter1Value = Binary(int(binaryInstruction[8:19], 2)).zfill(11)
            parameter1Value = self.getValue(parameter1Type, parameter1Value, registers, var_memory, stack)

            # PARAMETER 2 TYPE
            try:
                # Get the parameter2 type in binary (example: 0b00)
                parameter2Type = Binary(int(binaryInstruction[19:21], 2)).zfill(2)
                # Compare the parameter2 type with the OpType enum
                parameter2Type = OpType(int(parameter2Type, 2))
            except ValueError:
                raise Exception("Invalid parameter type.")
            
            # PARAMETER 2 VALUE
            parameter2Value = Binary(int(binaryInstruction[21:], 2)).zfill(11)
            parameter2Value = self.getValue(parameter2Type, parameter2Value, registers, var_memory, stack)

            # Write the decoded instruction in the file
            decodedFile.write(instructionOpcode + " " + parameter1Value + " " + parameter2Value + "\n")

    def getValue(self, type: OpType, number: str, registers: RegisterMemory, var_memory: VariableMemory, stack:Stack) -> str:
        match type:
            case OpType.VARIABLE:
                return var_memory.getData(int(number, 2)).name
            case OpType.REGISTER:
                return OpRegister(int(number, 2)).name
            case OpType.CONSTANT:
                return str(int(number, 2))

    def computeInstructions(self, registers: RegisterMemory, var_memory: VariableMemory, stack:Stack, step:bool) -> bool:
        '''
        The following function computes the instructions.
        '''

        # Open the decoded file
        decodedFile = open("./data/instructions/decodedFile.txt", "r")

        # Read the decoded file
        decodedInstructions = decodedFile.readlines()

        # Close the decoded file
        decodedFile.close()

        # Iterate through the decoded instructions
        counter = 0

        while True:

            print("\n")

            if counter >= len(decodedInstructions):
                break

            # Get the decoded instruction
            decodedInstruction = decodedInstructions[counter]
            
            # Remove the \n
            decodedInstruction = decodedInstruction.removesuffix("\n")

            # Split the decoded instruction into its components
            decodedInstruction = decodedInstruction.split(" ")

            # Get the instruction type
            instructionType = decodedInstruction[0]

            # Convert to enum to see if it exists
            try:
                instructionType = OpCode[instructionType]
            except KeyError:
                raise Exception("Invalid instruction type.")

            # See if the first parameter is valid
            try:
                parameter1Type = getParameterType(decodedInstruction[1])
                parameter2Type = getParameterType(decodedInstruction[2])
            except Exception:
                raise Exception("Invalid parameter type.")
            
            # Assign a class to the first parameter, according to its type
            if parameter1Type == OpType.REGISTER:
                parameter1 = Register(decodedInstruction[1], registers.getRegister(decodedInstruction[1]))
            elif parameter1Type == OpType.VARIABLE:
                parameter1 = var_memory.getDataByName(decodedInstruction[1])
            elif parameter1Type == OpType.CONSTANT:
                try:
                    parameter1 = Constant(int(decodedInstruction[1]))
                except ValueError:
                    raise Exception("Invalid constant.")
            else:
                raise Exception("Invalid parameter type.")

            # Assign a class to the second parameter, according to its type
            if parameter2Type == OpType.REGISTER:
                parameter2 = Register(decodedInstruction[2], registers.getRegister(decodedInstruction[2]))
            elif parameter2Type == OpType.VARIABLE:
                parameter2 = var_memory.getDataByName(decodedInstruction[2])
            elif parameter2Type == OpType.CONSTANT:
                try:
                    parameter2 = Constant(int(decodedInstruction[2]))
                except ValueError:
                    raise Exception("Invalid constant.")
            else:
                raise Exception("Invalid parameter type.")

            # Execute the function (inside data/OpFunctions.py with the same name as the instruction type
            try:
                op = OpFunctions()

                # Get the function dynamically
                func = op.__getattribute__(instructionType.name)

                # Check types
                hints = get_type_hints(func)
                for arg_name, arg_value in zip(func.__code__.co_varnames, [parameter1, parameter2, var_memory, registers, stack, counter]):
                    if arg_name in hints:
                        expected_type = hints[arg_name]
                        # Skip None type hints
                        if expected_type is not type(None) and not isinstance(arg_value, expected_type):
                            raise TypeError(f"{Color.RED.value}{instructionType.name} {parameter1.name} {parameter2.name}{Color.RESET.value} - Type mismatch for argument {arg_name}. Expected {expected_type}, got {type(arg_value)}.")

                # Execute the function
                counter = func(parameter1, parameter2, var_memory, registers, stack, counter)

                if counter == -1:
                    return True

            except AttributeError:
                raise Exception("Invalid instruction type.")
            
            print(f"{Color.BOLD.value}→{Color.GREEN.value} Current Instruction:{Color.WHITE.value}", instructionType.name, parameter1.name, parameter2.name)
            print(Color.RESET.value, end="")
            print(f"{Color.UNDERLINE.value}Memory:{Color.RESET.value}{Color.WHITE.value}")
            for register in registers.memory:
                print(f" {register} {Color.GRAY.value}{registers.memory[register]}{Color.WHITE.value}")
            
            print(f"{Color.UNDERLINE.value}Variables:{Color.RESET.value}{Color.WHITE.value}")
            for variable in var_memory.memory:
                # Print var name
                print(f" {var_memory.getVariableByAddress(variable).name} {Color.GRAY.value}{var_memory.memory[variable]}{Color.WHITE.value}")
            # Stack
            print(f"{Color.UNDERLINE.value}Stack:{Color.RESET.value}{Color.WHITE.value} {stack.__str__()}")
            
            print(f"{Color.UNDERLINE.value}Counter:{Color.RESET.value} {counter}")
            
            counter += 1

            if step and counter < len(decodedInstructions):
                input(Color.GREEN.value + "\n> Press enter to get to the next step..." + Color.RESET.value)
            elif step:
                input(Color.GREEN.value + "\n> Press enter to finish the program..." + Color.RESET.value)
                for _ in range(0, 10):
                    print("\n\n")

        return True