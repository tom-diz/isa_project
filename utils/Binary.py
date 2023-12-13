class Binary:
    def __init__(self, data: int|str):
        # If str startw with 0b, remove it and convert it to int
        if type(data) == str:
            if data[:2] == "0b":
                self.data:str = bin(int(data, 2))[2:]
            else:
                self.data:str = data
        if type(data) == int:
            self.data:str = bin(data)[2:]
        else:
            self.data:str = str(data)

    def __str__(self) -> str:
        return str(self.data)
    
    def __int__(self) -> int:
        return int(self.data, 2)
    
    def zfill(self, amount: int) -> str:
        '''
        The following function adds zeros to the left of the binary number.
        '''
        return self.data.zfill(amount)

    def __AND__(self, other: 'Binary') -> 'Binary':
        result = ''
        for i in range(len(self.data)):
            if self.data[i] == '1' and other.data[i] == '1':
                result += '1'
            else:
                result += '0'
        return Binary(result)
    
    def __OR__(self, other: 'Binary') -> 'Binary':
        result = ''
        for i in range(len(self.data)):
            if self.data[i] == '0' and other.data[i] == '0':
                result += '0'
            else:
                result += '1'
        return Binary(result)
    
    def __NOT__(self) -> 'Binary':
        result = ''
        for i in range(len(self.data)):
            if self.data[i] == '0':
                result += '1'
            else:
                result += '0'
        return Binary(result)
    
    def __INT__(self) -> int:
        data = self.data.lstrip('b')
        return int(data, 2)