import re
from functools import reduce
filename = "7_input.txt"

with open(filename, 'r') as filehandle:
    lines = filehandle.read().splitlines()

bags = []
res = []
numbers = []
def get_subbags(bag, amount):
    for line in lines:
        line = line.replace("bags","").split("contain")
        if bag in line[1]:
            amount = re.findall("(\\d+) " + bag, line[1])
            if bag != "shiny gold":
                numbers.append(int(amount[0]))
            print(line, bag)
            bags.append(line[0])
            get_subbags(line[0].strip(), numbers)
            print(numbers)
get_subbags("shiny gold", numbers)
[res.append(x) for x in bags if x not in res]
multi_num = reduce(lambda x, y: x*y, numbers)
print(len(res), len(bags), multi_num)
