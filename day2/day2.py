


file = open("input.txt", mode='r', encoding='utf-8-sig')
lines = file.readlines()
file.close()

def howManyAreAcceptable(list):
    count = 0

    for line in lines:
        array = line.split()
        letterparamater =array[1][0]
        paramaters = array[0].split("-")
        lowerparamater = int(paramaters[0])
        uperparamater =int(paramaters[1])
        if array[2][lowerparamater-1] == letterparamater and array[2][uperparamater-1] == letterparamater:
            continue
        elif array[2][lowerparamater-1] == letterparamater or array[2][uperparamater-1] == letterparamater:
            count += 1


    return count












print(howManyAreAcceptable(list))