import time
from collections import deque
import numpy as np
from numba import jit

@jit(nopython=True)
def find_first(item, vec):
    index = len(vec) - 1
    while index > -1:
        if item == vec[index]:
            return index
        index -= 1
    return -1

def read_file():
    input = "18,11,9,0,5,1"
    # input = "2,1,3"
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

def stupid_game2(data, loop_size):
    index = 1
    played_num = deque([data[0]])
    while index < loop_size:
        if played_num.count(played_num[0]) > 1:
            pos_1 = played_num.index(played_num[0])
            played_num.appendleft(played_num.index(played_num[0], pos_1 + 1) - pos_1)
        elif index < len(data):
            played_num.appendleft(data[index])
        else:
            played_num.appendleft(0)
        index += 1
    print(index, played_num[0])

def stupid_game3(data, loop_size):
    index = 1
    played_num = np.full(loop_size, -1, dtype=int)
    played_num[0] =data[0]
    selected = -1
    while index < loop_size:
        if np.sum(played_num[index -1] == played_num) > 1:
            pos = np.where(played_num == played_num[index -1 ])[0]
            played_num[index] = pos[-1] - pos[-2]
        elif index < len(data):
            played_num[index] = data[index]
        else:
            played_num[index] = 0
        index += 1
    print(index, played_num[-1])

def stupid_game4(data, loop_size):
    index = 1
    # played_num = np.full(loop_size, -1, dtype=np.int)
    played_num = np.array([],dtype=np.int)
    played_num = np.append(played_num, data[0])
    selected = -1
    while index < loop_size:
        played_num_tup = tuple([played_num[::]])
        print(played_num_tup[0])
        if played_num_tup.count(played_num[index -1]) > 1:
            pos_1 = played_num_tup.index(played_num_tup[index -1])
            played_num = np.append(played_num, pos_1 - played_num_tup[pos_1:].index(played_num_tup[index -1]))
        elif index < len(data):
            played_num = np.append(played_num,data[index])
        else:
            played_num = np.append(played_num, 0)
        index += 1
    print(index, played_num[0])

def run_task():
    data = read_file()
    size = 1000
    #      30000000
    # t0 = time.time()
    # stupid_game(data)
    # t1 = time.time()
    # print("aikaa meni:",round(t1-t0,4), "s")
    t0 = time.time()
    stupid_game3(data, size)
    t1 = time.time()
    print("aikaa meni:",round(t1-t0,4), "s")
    t0 = time.time()
    stupid_game4(data, size)
    t1 = time.time()
    print("aikaa meni:",round(t1-t0,4), "s")
    # stupid_game2(data)
    # print(data)

run_task()
