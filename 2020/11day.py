
import datetime
import time
from copy import deepcopy

def read_file():
    day = datetime.datetime.now().day
    file = str(day) + "_input.txt"
    # file = "testi.txt"
    with open(file, "r") as inputfile:
        data = [list(i.replace("L", "#")) for i in inputfile.read().splitlines()]

    return data
def draw_seat(data):
    count_occ = 0
    line = ""
    for idx_row,row in enumerate(data):
        for idx_seat,seat in enumerate(row):
            line += data[idx_row][idx_seat]
            if data[idx_row][idx_seat] == "#":
                count_occ += 1
        print(line)
        line = ''
    return count_occ


def what_seat(data_org):
    changes = 0
    data = deepcopy(data_org)
    for idx_row,row in enumerate(data):
        for idx_seat,seat in enumerate(row):
            start_row = idx_row - 1
            end_row = idx_row + 1

            if idx_row == 0:
                start_row = idx_row
            elif idx_row == (len(data) - 1):
                end_row = idx_row

            start_seat = idx_seat - 1
            end_seat = idx_seat + 1
            if idx_seat == 0:
                start_seat = idx_seat
            elif idx_seat == (len(row) - 1):
                end_seat = idx_seat
            count_occ = 0
            for i in range(start_row, end_row + 1):
                for k in range(start_seat, end_seat + 1):
                    mission_seat = data_org[i][k]
                    if [i,k] == [idx_row, idx_seat]:
                        continue
                    if mission_seat == "#":
                        count_occ += 1
            if count_occ == 0 and data[idx_row][idx_seat] == "L":
                data[idx_row][idx_seat] = "#"
                changes += 1
            elif count_occ > 3 and data[idx_row][idx_seat] == "#":
                data[idx_row][idx_seat] = "L"
                changes += 1
            # print(count_occ, idx_row,idx_seat, data[idx_row][idx_seat], data_org[idx_row][idx_seat])
    return changes, data

def what_seat_part2(data_org):
    changes = 0
    data = deepcopy(data_org)
    for idx_row,row in enumerate(data):
        for idx_seat,seat in enumerate(row):
            if data[idx_row][idx_seat] == ".":
                continue
            taken = [[".", -1, -1], [".", -1, 0], [".", -1, 1], [".", 0, 1], [".", 1, 1], [".", 1, 0], [".", 1, -1], [".", 0, -1]]
            # print( idx_row,idx_seat, data[idx_row][idx_seat])
            for direction in taken:
                for add_rounds in range(1,len(data_org) - 1):
                    check = [idx_row + add_rounds * direction[1],idx_seat + add_rounds * direction[2]]
                    # print(idx_row,idx_seat,add_rounds,direction[1],direction[2])
                    # print(check)
                    if check[0] < 0 or check[0] > len(data_org) - 1:
                        break
                    elif check[1] < 0 or check[1] > len(row) - 1:
                        break
                    if data_org[check[0]][check[1]] != ".":
                        direction[0] = data_org[check[0]][check[1]]
                        break
            count_occ = sum(x.count('#') for x in taken)
            # print( idx_row,idx_seat, data[idx_row][idx_seat],taken, count_occ)
            if count_occ == 0 and data[idx_row][idx_seat] == "L":
                data[idx_row][idx_seat] = "#"
                changes += 1
            elif count_occ > 4 and data[idx_row][idx_seat] == "#":
                data[idx_row][idx_seat] = "L"
                changes += 1
    return changes, data

def run_rules():
    t0 = time.time()
    data = read_file()
    changes = 0
    new_value = 0
    draw_seat(data)
    print("\n")
    while True:
        changes, data = what_seat_part2(data)
        print("varattuja istuimia",draw_seat(data))
        print("muutosten maara",changes, "\n")
        # break
        if changes == new_value:
            break
        new_value = changes
    t1 = time.time()
    print(round(t1-t0))

run_rules()
