
import datetime

def read_file():
    # file = str(datetime.datetime.now().day()) + "_input.txt"
    file = "8_input.txt"
    with open(file, "r") as inputfile:
        data = [i.split() for i in inputfile.read().splitlines()]
        data = [k + [0,"-"] for k in data]
    return data

def read_commants(commants):
    acc = 0
    index = 0
    change_index = 0
    change = 0
    change_mem_index = 0
    while True:
        commant = commants[index]
        # print(acc, change, change_index, index, commant, change_mem_index)
        if index == len(commants) -1 or change == len(commants) -1:
            # print("loppu", index, change)
            break
        if commant[2] == 1:
            for line in commants:
                line[2] = 0
            commants[change_mem_index][0] = commants[change_mem_index][3]
            change += 1
            index = 0
            change_index = 0
            acc = 0
            continue
        if change == change_index:
            if commant[0] == "jmp" or commant[0] == "nop":
                change_mem_index = index
            if commant[0] == "jmp":
                commant[0] = "nop"
                commant[3] = "jmp"
            elif commant[0] == "nop":
                commant[0] = "jmp"
                commant[3] = "nop"
        # print(commant)
        commant[2] = 1
        change_index += 1
        if commant[0] == "jmp":
            index += int(commant[1])
            continue
        elif commant[0] == "acc":
            acc += int(commant[1])
        index += 1



    return acc

def read_commants_back(commants):
    print(commants)
    index = len(commants) - 1
    roud = []
    while True:
        commant_2 = commants[index]
        position = 0
        if commant_2[2] == 1:
            print("toinen kierros")
            break
        commant_2[2] = 1
        roud.append(index)
        for i in range(len(commants) - 1, -1, -1):
            commant_back = commants[i]
            # print(index - i,i,index, commant_back)
            if commant_back[0] == "jmp":
                if int(commant_back[1]) == (index - i):
                    print(i, commants[i])
                    position = index - i
                    index = i
                    if index == 0:
                        return roud
                    break
        print(commant_back[1], position)
        if int(commant_back[1]) != position:
            index -= 1
            if commants[index][0] == "jmp":
                print("vituiks meni", index)
                break
    return roud


forward = read_commants(read_file())
print(forward)
