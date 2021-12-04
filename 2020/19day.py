import datetime
import time
from copy import deepcopy
import re
import itertools

def read_file():
    day = datetime.datetime.now().day
    # file = str(day) + "_input.txt"
    file = "testi.txt"
    with open(file, "r") as inputfile:
        data = [i for i in inputfile.read().splitlines()]
    group = []
    all = []
    for i in data:
        if i == "":
            all.append(group)
            group = []
        else:
            group.append(i.strip())
    all.append(group)
    return all

def get_rule(rules, data, sana, options):
    rules = rules.split(" | ")
    sets = []
    print("sisaan", sana, rules, options)
    possible = []
    for inde,i in enumerate(rules):
        tama_sana = ""
        set_i = []
        for k in i.split(" "):
            new_rule = data[int(k)].strip()
            rule_num = re.findall("(\\d+)", new_rule)
            if len(rule_num) < 1:
                tama_sana += new_rule.replace('"', '')
                if len(possible) > inde:
                    possible[inde] = tama_sana
                else:
                    possible.append(tama_sana)
                set_i.append(new_rule.replace('"', ''))
            else:
                print(options, possible)
                if len(possible) == 0:
                    possible = options
                # elif len(possible) != 0:
                #     options = [s+f for f in possible for s in options]
                # possible = []
                get_r, possible = get_rule(new_rule, data, sana + tama_sana, possible)
                set_i.append(get_r)
        print(tama_sana, possible, options)
        sets.append(set_i)
    options = [s+f for f in possible for s in options]
    print("vaihtoehdot", options)

    return sets, options

# def chek_valit_shit(stri, rules):


def get_monster(data):
    for ind,i in enumerate(data[0]):
        i = i.split(":")
        i[0] = int(i[0])
        data[0][ind] = i
    data[0].sort(key = lambda i: i[0])
    data[0] = [i[1].strip() for i in data[0]]
    all_rules = get_rule(data[0][0], data[0], "", [])
    print(all_rules)


def run_task():
    t0 = time.time()
    data = read_file()
    get_monster(data)
    t1 = time.time()
    print("aikaa meni:",round(t1-t0,4), "s")

run_task()
