
import datetime
import time
import itertools

def read_file():
    day = datetime.datetime.now().day
    file = str(day) + "_input.txt"
    # file = "testi.txt"
    with open(file, "r") as inputfile:
        data = [i.split(" = ") for i in inputfile.read().splitlines()]
    return data

def emulator(data):
    meamory = {}
    mask = 0
    mem = 0
    mem_sum = 0
    for line in data:
        if "mask" in line[0]:
            mask = line[1]
            continue
        elif "mem" in line[0]:
            mem = line[0][4:][:-1]
            num = bin(int(line[1]))[2:].zfill(36)
            print(num)
            for mask_index,mask_bit in enumerate(mask):
                if mask_bit != "X":
                    num = num[:mask_index] + mask_bit + num[mask_index+1:]
            print(num, int(num,2))
            meamory[mem] = int(num,2)
    for mem_s in meamory:
        if meamory[mem_s] != 0:
            mem_sum += meamory[mem_s]
    print(meamory)
    print(mem_sum)


def emulator_ver2(data):
    meamory = {}
    mask = 0
    mem = 0
    mem_sum = 0
    for line in data:
        if "mask" in line[0]:
            mask = line[1]
            continue
        elif "mem" in line[0]:
            mem = bin(int(line[0][4:][:-1]))[2:].zfill(36)
            num = int(line[1])
            mask_X_sum = mask.count("X")
            all_masks = [list(i) for i in itertools.product([0, 1], repeat=mask_X_sum)]
            for mask_bit_str in all_masks:
                mask_bit_index = 0
                for mask_index, mask_bit in enumerate(mask):
                    if mask_bit == "X":
                        mem = mem[:mask_index] + str(mask_bit_str[mask_bit_index]) + mem[mask_index+1:]
                        mask_bit_index += 1
                    elif mask_bit == "1":
                        mem = mem[:mask_index] + mask_bit + mem[mask_index+1:]
                print(mem, int(mem,2))
                meamory[int(mem,2)] = num
    for mem_s in meamory:
        # if meamory[mem_s] != 0:
        mem_sum += meamory[mem_s]
    print(meamory)
    print(mem_sum)


def run_task():
    t0 = time.time()
    data = read_file()
    emulator_ver2(data)
    t1 = time.time()
    # print(data)
    print(round(t1-t0))

run_task()
