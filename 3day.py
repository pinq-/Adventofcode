


filename = "3_input.txt"

with open(filename, 'r') as filehandle:
    lines = filehandle.readlines()
x = 0
three = 0
# for line in range(int(len(lines)/2)):
#     if (line * 2 + 1) == len(lines):
#         break
#     for i in range(1):
#         x += 1
#         if x == len(lines[0]) - 1:
#             x = 0
#
#     if lines[line*2 + 1][x] == "#":
#         three += 1
#         lines[line*2 + 1] = lines[line*2 + 1][:x] + 'X' + lines[line*2 + 1][x+1:]
#     else:
#         lines[line*2 + 1] = lines[line*2 + 1][:x] + 'O' + lines[line*2 + 1][x+1:]
#
#     # print(line + 1, x)
#     # print(lines[line*2 + 1])
y = 0
while(True):
    y += 2
    if (y + 1) == len(lines):
        break
    for i in range(1):
        x += 1
        if x == len(lines[0]) - 1:
            x = 0

    if lines[y][x] == "#":
        three += 1
        lines[y] = lines[y][:x] + 'X' + lines[y][x+1:]
    else:
        lines[y] = lines[y][:x] + 'O' + lines[y][x+1:]

        # print(line + 1, x)
        # print(lines[line*2 + 1])
print(three)
