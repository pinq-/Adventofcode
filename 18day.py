import datetime
import time
from pyparsing import *
import string, re
from copy import deepcopy

def read_file():
    day = datetime.datetime.now().day
    file = str(day) + "_input.txt"
    # file = "testi.txt"
    with open(file, "r") as inputfile:
        data = [i for i in inputfile.read().splitlines()]
    return data

def read_pracks(lista):
    tulos = 0
    line_in = 0
    while line_in < len(lista):

        item = lista[line_in]
        # print("item",item)
        if type(item) is not str:
            tulos += read_pracks(item)
            line_in += 1
        else:
            if item.isdigit():
                tulos += int(item)
            elif item is "(":
                line_in += 1
                continue
            elif item is ")":
                # print("tulos lopullinen",tulos)
                return tulos
            elif item == "*":
                if type(lista[line_in + 1]) is str:
                    tulos *= int(lista[line_in + 1])
                else:
                    tulos *= read_pracks(lista[line_in + 1])
                line_in += 1
            elif item == "+":
                if type(lista[line_in + 1]) is str:
                    tulos += int(lista[line_in + 1])
                else:
                    tulos += read_pracks(lista[line_in + 1])
                line_in += 1
            line_in += 1
        # print("tulos",tulos)
    return tulos

def read_pracks2(lista):
    lista = list(lista)
    for ind, item in enumerate(lista):
        if type(item) is not str:
            lista[ind]= read_pracks2(item)
    if "(" in lista:
        lista.remove("(")
    if ")" in lista:
        lista.remove(")")
    while lista.count("+") > 0:
        plus_in = lista.index("+")
        lista[plus_in+1] = int(lista[plus_in-1]) + int(lista[plus_in+1])
        lista = lista[:plus_in-1] + lista[plus_in+1:]
    while lista.count("*") > 0:
        plus_in = lista.index("*")
        lista[plus_in+1] = int(lista[plus_in-1]) * int(lista[plus_in+1])
        lista = lista[:plus_in-1] + lista[plus_in+1:]
    return lista[0]


def new_math(data):
    RawWord = Word(re.sub('[()" ]', '', string.printable))
    Token = Forward()
    Token << ( RawWord |
    Group('"' + OneOrMore(RawWord) + '"') |
    Group('(' + OneOrMore(Token) + ')') )
    Phrase = ZeroOrMore(Token)
    tulos_all = 0
    for line in data:

        if "(" in line:
            line = list(Phrase.parseString(line, parseAll=True))
            # print(line, "jee")
            tulos_all += read_pracks(line)
        else:
            line = line.split(" ")
            item_tulos = 0
            line_in = 0
            while line_in < len(line):
                item = line[line_in]
                # print(item)
                if item.isdigit():
                    item_tulos += int(item)
                elif item == "*":
                    item_tulos = item_tulos * int(line[line_in + 1])
                    line_in += 1
                elif item == "+":
                    item_tulos = item_tulos + int(line[line_in + 1])
                    line_in += 1
                line_in += 1
            tulos_all += item_tulos
    print(tulos_all)


def new_math2(data):
    RawWord = Word(re.sub('[()" ]', '', string.printable))
    Token = Forward()
    Token << ( RawWord |
    Group('"' + OneOrMore(RawWord) + '"') |
    Group('(' + OneOrMore(Token) + ')') )
    Phrase = ZeroOrMore(Token)
    tulos_all = 0
    for line in data:

        if "(" in line:
            line = Phrase.parseString(line, parseAll=True)
            # print(line, "jee")
            tulos_all += read_pracks2(line)
        else:
            line = line.split(" ")
            while line.count("+") > 0:
                plus_in = line.index("+")
                line[plus_in+1] = int(line[plus_in-1]) + int(line[plus_in+1])
                line = line[:plus_in-1] + line[plus_in+1:]
            while line.count("*") > 0:
                plus_in = line.index("*")
                line[plus_in+1] = int(line[plus_in-1]) * int(line[plus_in+1])
                line = line[:plus_in-1] + line[plus_in+1:]
            # print(line[0])
            tulos_all += line[0]
    print(tulos_all)

def run_task():
    t0 = time.time()
    data = read_file()
    new_math2(data)
    t1 = time.time()
    # print(data)
    print("aikaa meni:",round(t1-t0,4), "s")

run_task()
