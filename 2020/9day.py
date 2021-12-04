file = "9_input.txt"

with open(file, "r") as read_file:
    input = read_file.read().splitlines()
preamble = []
nono = 0

def if_sum(numbers, number):
    for i in range(len(numbers)):
        for k in range(len(numbers)):
            # print(i)
            if i == k:
                continue
            # print(numbers[i], numbers[k],numbers[i] + numbers[k], number)
            if numbers[i] + numbers[k] == int(number):
                # print(numbers[i] + numbers[k], number)
                return 0
    return 1

def get_set(numbers, the_one):
    for i in range(len(numbers)):
        winner = [int(numbers[i])]
        for k in numbers[i:]:
            if winner[0] == int(k):
                continue
            winner.append(int(k))
            # print(sum(winner), the_one)
            if sum(winner) == the_one:
                return winner
            elif sum(winner) > the_one:
                break
        # return 0

for number in input:
    if len(preamble) == 25:
        if if_sum(preamble, number) == 1:
            nono= number
            break
    if len(preamble) < 25:
        preamble.append(int(number))
        if len(preamble) != 25:
            continue
    elif len(preamble) == 25:
        preamble.append(int(number))
        preamble.pop(0)

print(nono)
kala = get_set(input, int(nono))
print(kala, min(kala)+max(kala))
