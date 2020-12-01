#Ratman64



file  = open("input.txt", mode='r', encoding="utf-8-sig" )
lines = file.readlines()

def find2020two(list):

    for i in range(len(list)):
        for j in range(len(list)):
            if int(list[i]) + int(list[j]) == 2020:
                return (int(list[i]) * int(list[j]))


def find2020three(list):
    for i in range(len(list))


print(find2020two(lines))