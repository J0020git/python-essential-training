def encodeString(stringVal):
    prevChar = stringVal[0]
    charLen = 0
    encodedList = []
    for char in stringVal:
        if char == prevChar:
            charLen = charLen + 1
        else:
            encodedList.append((prevChar, charLen))
            prevChar = char
            charLen = 1
    encodedList.append((prevChar, charLen))
    return encodedList


def decodeString(encodedList):
    stringVal = ""
    for char, len in encodedList:
        stringVal = stringVal + (char * len)
    return stringVal


encode1 = encodeString("Bookkeeping")
print(encode1)
decode1 = decodeString(encode1)
print(decode1)
