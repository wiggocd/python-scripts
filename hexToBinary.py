from typing import List
import math

hexLayout = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
hexLayoutStrings = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def getInput() -> str:
    string = input("\nPlease enter a number in hexadecimal or enter for default:\n\t> ")
    stringList = list(string)
    for i in range(len(stringList)):
        if hexLayoutStrings.__contains__(stringList[i]) == False:
            print("\nInput is not a hexadecimal number. Exiting...\n")
            exit()
    return string

def hexToBase10(string) -> int:
    ret = 0
    chars = list(string)

    for i in range(len(chars)):
        ret += hexLayoutStrings.index(chars[i]) * ( 16**(len(chars)-i-1))
        # H,T,U (n) = (h * n^2) + (t * n^1) + (u * n^0) where H=Hundreds, T=Tens, U=Units and N=Base.
        # e.g. 0x19F2 (base 16) = (1*16^3) + (9*16^2) + (15*16^1) + (2*16^0)

    return ret

def base10ToBin(number) -> int:
    ret: int
    bitLayout = []
    binaryList: List[int] = []

    for i in range(8):  # Change range for bit count
        bitLayout.insert(0, 2**i)

    for i in range(len(bitLayout)):
        tmp = math.floor(number / bitLayout[i])

        for x in range(len(binaryList)):
            if binaryList[x] != 0:
                tmp -= ( binaryList[x] * bitLayout[x] ) / bitLayout[i]

        binaryList.append(int(tmp))

    stringList = [ str(binaryList[i]) for i in range(len(binaryList)) ]
    ret = int( "".join(stringList) )
    return ret

def hexToBin(string):
    return base10ToBin(hexToBase10(string))

def hexListToBin(strings) -> List[str]:
    convertedList = []
    for i in range(len(strings)):
        convertedList.append(hexToBin(strings[i]))
    return convertedList

string = getInput()
converted = None
if string == "":
    defaultStrings = ["E2","3A","99","F8","5F"]
    print("\nHex strings to convert:", defaultStrings)
    converted = hexListToBin(defaultStrings)
else:
    converted = hexToBin(string)

print("\n____________\n")
print("Converted to binary:", converted)
print("____________\n")