import datetime
import time
import numpy as np
from copy import deepcopy

def read_file():
    day = datetime.datetime.now().day
    file = str(day) + "_input.txt"
    # file = "testi.txt"
    with open(file, "r") as inputfile:
        data = [i for i in inputfile.read().splitlines()]
    return data

def count_taken(grid,oz,oy,ox,size):
    if oz == 0:
        oz_start = 0
    else:
        oz_start = oz - size

    if oy == 0:
        oy_start = 0
    else:
        oy_start = oy - size

    if ox == 0:
        ox_start = 0
    else:
        ox_start = ox - size

    if oz == grid.shape[0] - 1:
        oz_end = grid.shape[0] - 1
    else:
        oz_end = oz + size + 1

    if oy == grid.shape[1] - 1:
        oy_end = grid.shape[1] - 1
    else:
        oy_end = oy + size + 1
    if ox == grid.shape[2] - 1:
        ox_end = grid.shape[2] - 1
    else:
        ox_end = ox + size + 1
    count = 0
    for z in range(oz_start,oz_end):
        for y in range(oy_start,oy_end):
            for x in range(ox_start,ox_end):
                if [z,y,x] == [oz,oy,ox]:
                    continue
                if grid[z,y,x] == 1:
                    count += 1
    return count

def count_taken2(grid,oz,oy,ox,ow,size):
    if oz == 0:
        oz_start = 0
    else:
        oz_start = oz - size

    if oy == 0:
        oy_start = 0
    else:
        oy_start = oy - size

    if ox == 0:
        ox_start = 0
    else:
        ox_start = ox - size
    if ow == 0:
        ow_start = 0
    else:
        ow_start = ow - size

    if oz == grid.shape[0] - 1:
        oz_end = grid.shape[0] - 1
    else:
        oz_end = oz + size + 1

    if oy == grid.shape[1] - 1:
        oy_end = grid.shape[1] - 1
    else:
        oy_end = oy + size + 1

    if ox == grid.shape[2] - 1:
        ox_end = grid.shape[2] - 1
    else:
        ox_end = ox + size + 1

    if ow == grid.shape[3] - 1:
        ow_end = grid.shape[3] - 1
    else:
        ow_end = ow + size + 1
    count = 0
    for z in range(oz_start,oz_end):
        for y in range(oy_start,oy_end):
            for x in range(ox_start,ox_end):
                for w in range(ow_start,ow_end):
                    if [z,y,x,w] == [oz,oy,ox,ow]:
                        continue
                    if grid[z,y,x,w] == 1:
                        count += 1
    return count

def cub_energy1(data):
    size= 2 * 4
    origo = [int(size/2),int(size/2)-2,int(size/2)-2]
    grid = np.zeros((size,size,size), dtype = "int")
    y = 0
    for i in data:
        x = 0
        for k in i:
            if k == "#":
                k = 1
            else:
                k = 0
            grid[origo[0],origo[1] + y,origo[2]+x] = k
            x+= 1
        y+= 1
    grid_sample = deepcopy(grid)
    print(grid)
    for i in range(6):
        print(i)
        for z,value_z in enumerate(grid):
            for y,value_y in enumerate(value_z):
                for x, value_x in enumerate(value_y):
                    taken = count_taken(grid_sample,z,y,x,1)
                    if grid_sample[z,y,x] == 1:
                        if 0 in [z,y,x] or size-1 in [z,y,x]:
                            print("raja tuli vastaan, ei hyvä", [z,y,x])
                            return 0
                        if taken < 2 or taken > 3:
                            grid[z,y,x] = 0
                    else:
                        if taken == 3:
                            grid[z,y,x] = 1
        grid_sample = deepcopy(grid)
        # print(grid)
        print(np.count_nonzero(grid))


def cub_energy2(data):
    size= 2 * 15
    origo = [int(size/2),int(size/2)-2,int(size/2)-2, int(size/2)]
    grid = np.zeros((size,size,size,size), dtype = "int")
    y = 0
    for i in data:
        x = 0
        for k in i:
            if k == "#":
                k = 1
            else:
                k = 0
            grid[origo[0],origo[1] + y,origo[2]+x, origo[3]] = k
            x+= 1
        y+= 1
    grid_sample = deepcopy(grid)
    print(grid)
    for i in range(6):
        print(i)
        for z,value_z in enumerate(grid):
            for y,value_y in enumerate(value_z):
                for x, value_x in enumerate(value_y):
                    for w, value_w in enumerate(value_x):
                        taken = count_taken2(grid_sample,z,y,x,w,1)
                        if grid_sample[z,y,x,w] == 1:
                            if 0 in [z,y,x,w] or size-1 in [z,y,x,w]:
                                print("raja tuli vastaan, ei hyvä", [z,y,x,w])
                                return 0
                            if taken < 2 or taken > 3:
                                grid[z,y,x,w] = 0
                        else:
                            if taken == 3:
                                grid[z,y,x,w] = 1

        grid_sample = deepcopy(grid)
        # print(grid)
        print(np.count_nonzero(grid))
def run_task():
    t0 = time.time()
    data = read_file()
    # cub_energy1(data)
    cub_energy2(data)
    t1 = time.time()
    print(data)
    print("aikaa meni:",round(t1-t0,4), "s")

run_task()
