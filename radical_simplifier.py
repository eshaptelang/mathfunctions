isNeg = 0
numList = []
endNumDict = {}
keyPopList = []
def primeFactors():
    if (number ** 0.5) % 1== 0:
        print("The number you gave was a perfect square root. The answer would be: " + str(number ** 0.5))
    else:
        i = 1
        newNum = number
        while i <= newNum/2:
            i = i + 1
            if newNum % i == 0:
                newNum = newNum / i
                numList.append(i)
                i = 1
        numList.append(newNum)


numDict = {}
def sort():
    numList.sort()
    x = 0
    while x < len(numList):
        if numList[x] not in numDict.keys():
            numDict[numList[x]] = 1
        else:
            numDict[numList[x]] = numDict[numList[x]] + 1
        x = x + 1

def find():
    y = 0
    for key in numDict:
        if numDict[key] > 1:
            if numDict[key] % 2 == 0:
                endNumDict[key] = numDict[key]/2
                keyPopList.append(key)
            else:
                endNumDict[key] = (numDict[key] - 1) / 2
                numDict[key] = 1
    for thing in keyPopList:
        numDict.pop(thing)

def create():
    finalBeg = 1
    finalEnd = 1
    z = 0
    for key in numDict:
        finalBeg = key * finalBeg
    for key in endNumDict:
        finalEnd = finalEnd * (key ** endNumDict[key])
    if isNeg == 1:
        print("The simplified radical is: " + str(finalEnd) + "i times the square root of " + str(finalBeg))
    else:
        print("The simplified radical is: " + str(finalEnd) + " times the square root of " + str(finalBeg))







number = input("Square root of: ")
if type(number) == int:
    if number > 0:
        primeFactors()
        sort()
        find()
        create()
    else:
        isNeg = 1
        number = abs(number)
        primeFactors()
        sort()
        find()
        create()
else:
    while type(number) != int:
        number = input("Enter number would you like simplifyed: ")
    if number > 0:
        primeFactors()
        sort()
        find()
        create()
    else:
        isNeg = 1
        number = abs(number)
        primeFactors()
        sort()
        find()
        create()



