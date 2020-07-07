alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def getInput():
    string = input("\nPlease enter a string without numbers or special characters:\n\t> ")
    for i in range(len(string)):
        if alphabet.__contains__(string[i].upper()) == False:
            print("\nString contains a number or special character. Exiting...\n")
            exit()
    return string

def convert(string):
    ret = None
    stringList = list(string)
    convertedList = []
    for i in range(len(string)):
        index = alphabet.index(stringList[i])-3
        if index < 0:
            index = len(alphabet) + index   # + as the index is negative
        convertedList.append(alphabet[index])

    ret = "".join(convertedList)
    return ret

string = getInput()
ret = convert(string)
print("\n____________\n")
print("Converted with the Caeser Cipher:", ret)
print("____________\n")
exit()