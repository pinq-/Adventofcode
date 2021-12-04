import re
filename = "4_input.txt"
valid_passport = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
def Convert(lst):
    list2 = []
    for element in lst:
        list2.extend(element.split(":"))
    res_dct = {list2[i]: list2[i + 1] for i in range(0, len(list2), 2)}
    return res_dct

def test_case(passport):
    dic_passport = Convert(passport)
    dic_keys = list(dic_passport.keys())
    if all(x in dic_keys for x in valid_passport):
        if test_bday(dic_passport["byr"]) and\
            test_iday(dic_passport["iyr"]) and\
            test_eday(dic_passport["eyr"]) and\
            test_hgt(dic_passport["hgt"]) and\
            test_hcl(dic_passport["hcl"]) and\
            test_ecl(dic_passport["ecl"]) and\
            test_pid(dic_passport["pid"]):
            return 1
        else:
            return 0
    else:
        return 0

def test_bday(year):
    if len(year) == 4 and year.isnumeric():
        year = int(year)
        if year <= 2002 and year >= 1920:
            return True
    return False

def test_iday(year):
    if len(year) == 4 and year.isnumeric():
        year = int(year)
        if year <= 2020 and year >= 2010:
            return True
    return False

def test_eday(year):
    if len(year) == 4 and year.isnumeric():
        year = int(year)
        if year <= 2030 and year >= 2020:
            return True
    return False

def test_hgt(hgt):
    if hgt[:-2].isnumeric():
        high = int(hgt[:-2])
        if hgt[-2:] == "cm":
            if high >= 150 and high <= 193:
                return 1
        if hgt[-2:] == "in":
            if high >= 59 and high <= 76:
                return 1
    return 0

def test_hcl(hcl):
    if hcl[0] == "#":
        if len(hcl[1:]) == 6:
            for i in hcl[1:]:
                if i.isnumeric() == False:
                    if i > "f":
                        return False
            return True
    return False

def test_ecl(ecl):
    if len(ecl) == 3:
        if ecl in eyes:
            return True
    return False

def test_pid(pid):
    if len(pid) == 9:
        if pid.isnumeric():
            return True

    return False



with open(filename, 'r') as filehandle:
    lines = filehandle.readlines()

passports = []
passport = []
amount_valid = 0
for line in lines:
    if line == "\n":
        amount_valid += test_case(passport)
        passport = []
        continue

    passport.extend(line.strip().split(" "))
amount_valid += test_case(passport)
print(amount_valid)
