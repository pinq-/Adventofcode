import datetime
import time
from pyparsing import *
import string, re
from copy import deepcopy

def read_file():
    day = datetime.datetime.now().day
    # file = str(day) + "_input.txt"
    file = "testi.txt"
    with open(file, "r") as inputfile:
        data = [i.split(" (contains ") for i in inputfile.read().splitlines()]
    return data

def make_som_food(data):
    for ik in data[0]:
        ik = ik.split(" ")

def run_task():
    t0 = time.time()
    data = read_file()
    t1 = time.time()
    print(data)
    print("aikaa meni:",round(t1-t0,4), "s")

run_task()
