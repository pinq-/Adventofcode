import datetime
import time
import itertools

def read_file():
    day = datetime.datetime.now().day
    file = str(day) + "_input.txt"
    # file = "testi.txt"
    with open(file, "r") as inputfile:
        data = [i for i in inputfile.readlines()]
    group = []
    all = []
    for i in data:
        if i == "\n":
            all.append(group)
            group = []
        else:
            group.append(i.strip())
    all.append(group)
    return all

def valid_tickets(data):
    rules = set()
    for rule in data[0]:
        numbers = rule.split(":")
        numbers = numbers[1].split(" ")
        rule1 = numbers[1].split("-")
        rule2 = numbers[3].split("-")
        [rules.add(i) for i in range(int(rule1[0]), int(rule1[1]) + 1)]
        [rules.add(i) for i in range(int(rule2[0]), int(rule2[1]) + 1)]
    invalid = []
    tickets = data[2][1::].copy()
    for ticket in data[2][1::]:
        for num in ticket.split(","):
            if int(num) not in rules:
                invalid.append(int(num))
                if ticket in tickets:
                    tickets.remove(ticket)
    tickets = [i.split(",") for i in tickets]
    return tickets

def valid_tickets2(data):
    rules_class = {}
    for rule in data[0]:
        clasees = rule.split(":")
        numbers = clasees[1].split(" ")
        rule1 = numbers[1].split("-")
        rule2 = numbers[3].split("-")
        rules_class[clasees[0]] = []
        [rules_class[clasees[0]].append(i) for i in range(int(rule1[0]), int(rule1[1]) + 1)]
        [rules_class[clasees[0]].append(i) for i in range(int(rule2[0]), int(rule2[1]) + 1)]
    tickets = valid_tickets(data)
    class_keys = list(rules_class.keys())
    right_order = [0] * len(class_keys)
    while True:
        if 0 not in right_order:
            break
        columns = 0
        while columns < len(tickets[0]):
            if right_order[columns] != 0:
                columns += 1
                continue
            rules_valid = []
            for rule in class_keys:
                if rule in right_order:
                    rules_valid.append(0)
                    continue
                count = 0
                for ticket in tickets:
                    if int(ticket[columns]) in rules_class[rule]:
                        count += 1
                rules_valid.append(count)
            if rules_valid.count(len(tickets)) == 1:
                right_order[columns] = class_keys[rules_valid.index(len(tickets))]
                columns = 0
                continue
            columns += 1
    yhteen = 1
    your_ticket = data[1][1].split(",")
    for ind,r_class in enumerate(right_order):
        if "departure" in r_class:
            yhteen *= int(your_ticket[ind])
    print(yhteen)

def run_task():
    t0 = time.time()
    data = read_file()
    valid_tickets2(data)
    t1 = time.time()
    # print(data)
    print("aikaa meni:",round(t1-t0,4), "s")

run_task()
