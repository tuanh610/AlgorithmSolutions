def DecToBinaryString(a):
    stack = []
    while a > 0:
        stack.append(str(a%2))
        a = a//2
    stack.reverse()
    return "".join(stack)


def BinaryStringToDec(a):
    res = 0
    for i in range(len(a)-1,-1,-1):
        order = len(a) - 1- i
        res += int(a[i])*(2**order)
    return res

def getBit(num, idx):
    return (num & (1 << idx)) != 0

def setBit(num, idx):
    return (num | (1 << idx))

def clearBit(num, idx):
    mask = ~(1 << idx)
    return (num & mask)

def clearBitFromStart(num, idx):
    if idx < 0:
        return num
    mask = (-1 << idx+1)
    return (num & mask)

def clearBitTillEnd(num, idx):
    mask = (1 << idx) - 1
    return (num & mask)
