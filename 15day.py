import time
from collections import deque
import numpy as np

def read_file():
    # input = "18,11,9,0,5,1"
    input = "0,3,6"
    input = input.split(",")
    data = [int(i) for i in input]
    return data

def stupid_game(data):
    index = 0
    played_num = []
    selected = -1
    while index < 2020:
        if selected != -1 and played_num.count(selected) > 1:
            pos = [i + 1 for i, x in enumerate(played_num) if x == selected]
            dif = pos[-1] - pos[-2]
            selected = dif
        elif index > len(data) - 1:
            selected = 0
        elif index < len(data):
            selected = data[index]
        played_num.append(selected)
        index += 1
        # print(index)
    print(index, selected, len(played_num))

def stupid_game2(data):
    index = 1
    played_num = deque([data[0]])
    selected = -1
    while index < 30000000:
        if played_num.count(played_num[0]) > 1:
            pos_1 = played_num.index(played_num[0])
            played_num.appendleft(played_num.index(played_num[0], pos_1 + 1) - pos_1)
        elif index < len(data):
            played_num.appendleft(data[index])
        else:
            played_num.appendleft(0)
        index += 1
        # print(index, played_num)
        # print(index)
    print(index, selected)

def stupid_game3(data):
    index = 1
    loop_size = 2020
    played_num = np.empty(loop_size, dtype=int)
    np.append(played_num,data[0])
    selected = -1
    while index < loop_size:
        if np.sum(played_num[0] == played_num) > 1:
            dif = np.where(played_num, played_num[0])[]
            np.where(played_num, played_num[0]))
        elif index < len(data):
            played_num.appendleft(data[index])
        else:
            played_num.appendleft(0)
        index += 1
        # print(index, played_num)
        # print(index)
    print(index, selected)

def run_task():
    t0 = time.time()
    data = read_file()
    stupid_game(data)
    # stupid_game2(data)
    t1 = time.time()
    # print(data)
    print("aikaa meni:",round(t1-t0,4), "s")

run_task()
