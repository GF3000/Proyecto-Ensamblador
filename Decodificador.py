def hexCharToAscii(hexChar):
    return chr(int(hexChar, 16))

def hexStringToAscii(hexString):
    return ''.join([hexCharToAscii(hexChar) for hexChar in hexString.split()])

def multipleNinBinario(n):
    return [bin(i)[2:] for i in range(0, 256, n)]
#hexChars = "74 72 65 73 20 74 72 69 73 74 65 73 20 74 69 67 72 65 73 20 63 6F 6D 65 6E 20 74 72 69 67 6F 20 65 6E 20 75 6E 20 74 72 69 67 61 6C 2C 20 65 6C 20 70 72 69 6D 65 72 20 74 69 67 72 65 20 71 75 65 2E 2E 2E"
#print(hexCharToAscii("6E"))
print(len("tres tristes tigres comen trigo en un trigal, el primer tigre que..."))
#print (multipleNinBinario(4))