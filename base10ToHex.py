import math

def getInput():
    string = input("\nPlease enter an integer between 0 and 255.\n\t> ")
    ret = int(string)

    if 0 < ret < 256:
        return ret
    else:
        print("\nInput is not an integer between 0 and 255. Exiting...\n")
        exit()

def convert(value):
    ret = None
    number = int(value)
    hexLayout = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    convertedList = []

    if number > 15:
        initialFloor = math.floor(number / 16)
        floor = initialFloor

        while floor > 0:
            convertedList.append(floor)
            floor = number - 16*initialFloor
            for i in range(1, len(convertedList)):
                floor -= 16*convertedList[i-1]
        
    else:
        convertedList.append(number)
    
    for i in range(len(convertedList)):
        convertedList[i] = hexLayout[convertedList[i]]

    stringList = [ str(convertedList[i]) for i in range(len(convertedList))]
    ret = "".join(stringList)
    return ret

number = getInput()
hexadecimal = convert(number)
print("_____________\n")
print("Converted to hex:", hexadecimal)
print("_____________\n")
exit()