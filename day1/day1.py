#Ratman64



file  = open("input.txt", mode='r', encoding="utf-8-sig")
lines = file.readlines()
file.close()

def find2020two(list):

    for i in range(len(list)):
        for j in range(len(list)):
            if int(list[i]) + int(list[j]) == 2020:
                return (int(list[i]) * int(list[j]))


def find2020three(list):
    for i in range(len(list)):
        for j in range(len(list)):
            for b in range(len(list)):
                if int(list[i])+ int(list[j]) + int(list[b]) == 2020:
                    return int(list[i])* int(list[j]) * int(list[b])


print(find2020two(lines))
print(find2020three(lines))