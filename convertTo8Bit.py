import math

def inputHandler():
    string = input("\nPlease enter an integer between 0 and 255.\n\t> ")
    ret = int(string)

    if 0 < ret < 256:
        return ret
    else:
        print("\nInput is not an integer between 0 and 255. Exiting...\n")
        exit()

def convert(value):
    number = int(value)
    binaryArray = []
    bitLayout = []

    for i in range(8):
        bitLayout.insert(0, 2**i)
    print("Binary layout:", bitLayout)

    for i in range(len(bitLayout)):
        tmp = math.floor(number / bitLayout[i])
        print("\tBit", i, ": Division floor before subtraction:", tmp)

        for x in range(len(binaryArray)):
            if binaryArray[x] != 0:
                tmp -= ( bitLayout[x] * binaryArray[x] ) / bitLayout[i]
            print("\tFloor subtraction", x, ":", tmp)
        
        binaryArray.append(int(tmp))

    print("Array:", binaryArray)
    stringList = [ str(binaryArray[i]) for i in range(len(binaryArray)) ]

    return int("".join(stringList))


number = inputHandler()
binary = convert(number)
print("___________________\n")
print("Converted to 8-bit binary:", binary)
print("___________________")
exit()