
import datetime
hit_end = 1
import time
from copy import deepcopy
import math
def read_file():
    day = datetime.datetime.now().day
    # file = "10_input.txt"
    file = "testi.txt"
    with open(file, "r") as inputfile:
        data = [int(i) for i in inputfile.read().splitlines()]

    return data

def get_jolts(data):
    data.append(0)
    data.sort()
    # print(data)
    jolts_dif = {1:0,2:0,3:0}
    for adabter in range(len(data)):
        if adabter == len(data) - 1:
            jolts_dif[3] += 1
            break
        # print(data[adabter + 1] - data[adabter], data[adabter + 1], data[adabter])
        jolts_dif[data[adabter + 1] - data[adabter]] += 1
    return jolts_dif


def joltsjolts(data, index, hitend):
    data.sort()
    steps = []
    routes = []
    for i in range(len(data)):
        print("order",data[i])
        count_jumps = 1
        routes_c = deepcopy(routes)
        for rout in routes_c:
            if rout[0] != data[i]:
                routes.remove(rout)
        for k in range(2,4):
            if i < len(data) - k:
                next = data[i + k]
                if (data[i + k] - data[i]) >3:
                    break
                print(data[i + k])
                if (data[i + k] - data[i]) == 2:
                    if [data[i], data[i + k]] in routes:
                        continue
                    routes.append([data[i], data[i + k]])
                    count_jumps += 1
                elif (data[i + k] - data[i]) == 3:
                    routes.append([data[i], data[i + k]])
                    routes.append([data[i + 1], data[i + k]])
                    count_jumps += 2
                print("lisa",data[i + k], data[i + k] - data[i], count_jumps)
        # if count_jumps > 1:
        print(routes)
        steps.append(count_jumps)
    result = 0
    result2 = 1
    for x in steps:
         result += math.factorial(x)
         result2 *= x
    print(result, result2, sum(steps) + 1, steps)
t0 = time.time()
data = read_file()
data.append(0)
data.sort()
print(data)
joltsjolts(data, 0, [])
t1 = time.time()
print(hit_end, round(t1-t0,3))
