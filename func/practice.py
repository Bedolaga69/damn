def getCountedListRec(cap, numList):
    cap_left = cap
    countedList = [0] * len(numList)
    i = 0
    f = False
    while not f:
        step = 0
        steps = 1
        while i > 0:
            i -= 1
            if countedList[i] > 0:
                countedList[i] -= 1
                cap_left += numList[i]
                i += 1
                step += 1
                if i == len(numList):
                    steps += 1
                if step == steps:
                    break
        if i == 0:
            return countedList
        while i < len(numList):
            if cap_left - numList[i] >= 0:
                cap_left -= numList[i]
                countedList[i] += 1
            else:
                i += 1
        if cap_left == 0:
            f = True
    return countedList



weightString = input("Введите список значений: ")
startValue = int(input("Введите стартовое значение: "))
endValue = int(input("Введите значений, которое хотите получить: "))
sumValue = startValue - endValue
weightList = [int(item) for item in weightString.split(" ")]
weightList.sort(reverse=True)
countList = getCountedListRec(sumValue, weightList)
print(weightList)
print([str(countList[i])+"*"+str(weightList[i]) for i in range(len(countList))])