import numpy as np

def test_if_in_area(shape, point):
    if point[0] < 0 or point[0] > shape[0] - 1 or point[1] < 0 or point[1] > shape[1] - 1:
        return False
    else:
        return True
    
def return_adjacents(point, diagonal = 0):
    if diagonal:
        return [(point[0] - 1 , point[1] - 1), (point[0] - 1 , point[1]), (point[0] - 1 , point[1] + 1), (point[0] , point[1] - 1), (point[0] , point[1] + 1), (point[0] + 1 , point[1] - 1), (point[0] + 1 , point[1]), (point[0] + 1 , point[1] + 1)]
    else:
        return  [(point[0] - 1 , point[1]), (point[0] , point[1] - 1), (point[0] , point[1] + 1), (point[0] + 1 , point[1])]
    