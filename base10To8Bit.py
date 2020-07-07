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
    number = int(value)
    binaryList = []
    bitLayout = []

    for i in range(8):
        bitLayout.insert(0, 2**i)
    print("Binary layout:", bitLayout)

    for i in range(len(bitLayout)):
        tmp = math.floor(number / bitLayout[i])
        print("\tBit", i, ": Division floor before subtraction:", tmp)

        for x in range(len(binaryList)):
            if binaryList[x] != 0:
                tmp -= ( bitLayout[x] * binaryList[x] ) / bitLayout[i]
            print("\tFloor subtraction", x, ":", tmp)
        
        binaryList.append(int(tmp))

    print("Array:", binaryList)
    stringList = [ str(binaryList[i]) for i in range(len(binaryList)) ]

    return int("".join(stringList))


number = getInput()
binary = convert(number)
print("___________________\n")
print("Converted to 8-bit binary:", binary)
print("___________________")
exit()