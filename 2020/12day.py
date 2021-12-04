
import datetime
import time
from copy import deepcopy
from math import cos, sin, radians

def read_file():
    day = datetime.datetime.now().day
    file = str(day) + "_input.txt"
    # file = "testi.txt"
    with open(file, "r") as inputfile:
        data = [[i[:1],int(i[1:])] for i in inputfile.read().splitlines()]
    return data

def angle_to_direciton(ship):
    if ship["angle"] == 0 and ship["direction"] != "S":
        ship["direction"] = "S"
    elif ship["angle"] == 90 and ship["direction"] != "E":
        ship["direction"] = "E"
    elif ship["angle"] == 180 and ship["direction"] != "N":
        ship["direction"] = "N"
    elif ship["angle"] == 270 and ship["direction"] != "W":
        ship["direction"] = "W"
    return ship

def run_the_ship(data):
    directions = ["S", "E", "N", "W"]
    ship = {"E":0,"W": 0, "N":0,"S":0, "direction":"E",  "angle":90}
    waypoint = {"E":0,"W": 0, "N":0,"S":0}
    for commant in data:
        if commant[0] == "F":
            ship[ship["direction"]] += commant[1]
            continue
        elif commant[0] == "L":
            ship["angle"] += commant[1]
            if ship["angle"] > 270:
                ship["angle"] -= 360
            ship = angle_to_direciton(ship)
        elif commant[0] == "R":
            ship["angle"] -= commant[1]
            if ship["angle"] < 0:
                ship["angle"] += 360
            ship = angle_to_direciton(ship)
        elif commant[0] in directions:
            ship[commant[0]] += commant[1]
    S_N = ship["N"] * -1 + ship["S"]
    E_W = ship["E"] * -1 + ship["W"]
    print(ship)
    return abs(S_N) + abs(E_W)

def rotate_vector(waypoint, angle):
    angle_rad = radians(angle % 360)
    # Shift the point so that center_point becomes the origin
    new_point = (waypoint["S_N"] * cos(angle_rad) - waypoint["W_E"] * sin(angle_rad),
                 waypoint["S_N"] * sin(angle_rad) + waypoint["W_E"] * cos(angle_rad))
    # Reverse the shifting we have done
    waypoint["S_N"] = round(new_point[0])
    waypoint["W_E"] = round(new_point[1])
    return waypoint


def run_the_ship_part2(data):
    ship = {"S_N":0, "W_E":0}
    waypoint = {"S_N":1,"W_E": 10}
    for commant in data:
        # print("Lahto",waypoint, ship)
        if commant[0] == "F":
            ship["S_N"] += waypoint["S_N"] * commant[1]
            ship["W_E"] += waypoint["W_E"] * commant[1]
        elif commant[0] == "L":
            waypoint = rotate_vector(waypoint, -1 *commant[1])
        elif commant[0] == "R":
            waypoint = rotate_vector(waypoint, commant[1])
        elif commant[0] == "N" or commant[0] == "S":
            if commant[0] == "N":
                waypoint["S_N"] += commant[1]
            else:
                waypoint["S_N"] -= commant[1]
        elif commant[0] == "W" or commant[0] == "E":
            if commant[0] == "E":
                waypoint["W_E"] += commant[1]
            else:
                waypoint["W_E"] -= commant[1]
        # print("Loppu",waypoint, ship)
    print(ship)
    return abs(ship["S_N"]) + abs(ship["W_E"])



def run_task():
    t0 = time.time()
    data = read_file()
    print(run_the_ship_part2(data))
    t1 = time.time()
    print(data)
    print(round(t1-t0))

run_task()
