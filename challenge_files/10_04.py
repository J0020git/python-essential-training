import json


def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList


def decodeString(encodedList):
    decodedStr = ""
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr


# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    with open(filename, "r") as originalFile:
        newFile = open(newFilename, "w")
        stringVal = ""
        for line in originalFile.readlines():
            stringVal = stringVal + line
        encodedList = encodeString(stringVal)
        encodedString = json.dumps(encodedList)
        newFile.write(encodedString)
        newFile.close()


def decodeFile(filename):
    with open(filename, "r") as encodedFile:
        encodedString = ""
        for line in encodedFile.readlines():
            encodedString = encodedString + line
        encodedList = json.loads(encodedString)
        stringVal = decodeString(encodedList)
        return stringVal