import datetime
import time
import itertools

def read_file():
    day = datetime.datetime.now().day
    # file =  "13_input.txt"
    file = "testi.txt"
    with open(file, "r") as inputfile:
        data = [i for i in inputfile.read().splitlines()]
    return data

def eka_tehtava(data):
    time_a = int(data[0])
    buss_num = data[1].replace("x,","")
    buss_num = buss_num.split(",")
    smallest = [-1, 0]
    for bus in buss_num:
        bus = int(bus)
        wait_t = (bus*(time_a / bus - time_a % bus / bus) + bus ) - time_a
        print(bus, time_a, wait_t)
        if smallest[0] == -1:
            smallest[0] = wait_t
            smallest[1] = bus
        elif smallest[0] > wait_t:
            smallest[0] = wait_t
            smallest[1] = bus
    print(smallest[0]* smallest[1])

def toka_tehtava(data):
    buss_num = data[1].split(",")
    busses = []
    for inte, bus in enumerate(buss_num):
        if bus != "x":
            busses.append([bus,inte])
    all = 1
    # print(busses)
    jakaja = 0
    tekija = 0
    for bus in busses:
        all *= int(bus[0])
        yhteen = 1
        for jaka in busses:
            if jaka[1] != bus[1]:
                yhteen *= int(jaka[0])
        tekija += bus[1] * yhteen
        jakaja += yhteen
        # print(all, jakaja, tekija)
    n = 0
    x = 0
    first = 0
    while True:
        x = (all*n - tekija) / jakaja
        # print((all*n - tekija) / jakaja)
        if x - round(x) == 0:
            if first == 1:
                break
            else:
                first = 1
        n+=1
    print("tulos",x,n)

def run_task():
    t0 = time.time()
    data = read_file()
    # print(data)
    # eka_tehtava(data)
    toka_tehtava(data)
    t1 = time.time()
    print("aikaa meni:",round(t1-t0,4), "s")

run_task()
