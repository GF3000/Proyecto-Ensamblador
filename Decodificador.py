def hexCharToAscii(hexChar):
    return chr(int(hexChar, 16))

def hexStringToAscii(hexString):
    return ''.join([hexCharToAscii(hexChar) for hexChar in hexString.split()])

hexChars = "54 72 65 73 54 72 69 73 74 65 73 54 69 67 01 0A 01 45 6E FF 07 01 67 61 6C 65 73"
print(hexStringToAscii(hexChars))
print(hexCharToAscii("6E"))
print(len(TresTristesTigresTristesEnTresTrigales"))