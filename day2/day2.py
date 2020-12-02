


file = open("input.txt", mode='r', encoding='utf-8-sig')
lines = file.readlines()
file.close()

def howManyAreAcceptable(list):
    count = 0

    for line in lines:
        array = line.split()
        letterparamater =array[1][0]
        paramaters = array[0].split("-")
        lowerparamater = paramaters[0]
        uperparamater =paramaters[1]
        lettercount = 0
        for letter in array[2]:
            if letter == letterparamater:
                lettercount +=1

        if lettercount >= int(lowerparamater) and lettercount <= int(uperparamater):
            count += 1
    return count












print(howManyAreAcceptable(list))