import datetime
import pandas as pd
import numpy as np
filename = "5_input.txt"
rows = 128
cloumn = 8
with open(filename, 'r') as filehandle:
    lines = filehandle.readlines()

def get_id(id_num):
    bf = id_num[:-3]
    lr = id_num[-3:]
    bf_row = [i for i in range(rows)]
    lr_row = [i for i in range(cloumn)]
    for i in bf:
        size = len(bf_row)
        if i == "F":
            bf_row = bf_row[:int(size/2)]
        else:
            bf_row = bf_row[int(size/2):]
    for i in lr:
        size = len(lr_row)
        if i == "L":
            lr_row = lr_row[:int(size/2)]
        else:
            lr_row = lr_row[int(size/2):]
    return [bf_row[0], lr_row[0], bf_row[0] * 8 + lr_row[0]]

def test_line(lines):
    max_id = 0
    for line in lines:
        id = get_id(line.strip())
        # print(line)
        if id[2] > max_id:
            max_id = id[2]
            print(max_id, line)
# test_line(lines)

def find_seat(lines):
    matrix_2 = np.full((rows, cloumn), False)
    for line in lines:
        id = get_id(line.strip())
        matrix_2[id[0]][id[1]] = True
    my_row = int(np.where(np.count_nonzero(matrix_2, axis=1) ==7)[0])
    my_col = int(np.where(matrix_2[my_row,:] == False)[0])
    print(my_row, my_col, my_row * 8 + my_col)
find_seat(lines)
