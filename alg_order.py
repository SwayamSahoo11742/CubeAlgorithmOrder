from Cube import Cube
import math
from functools import reduce
SOLVED_STATE = {
    "F": [[1,2,3], [4,5,6], [7,8,9]],
    "R": [[10,11,12], [13,14,15], [16,17,18]],
    "B": [[19,20,21], [22,23,24], [25,26,27]],
    "L": [[28,29,30], [31,32,33], [34,35,36]],
    "U": [[37,38,39], [40,41,42], [43,44,45]],
    "D": [[46,47,48], [49,50,51], [52,53,54]]
}

def calculate_order(alg:str):
    visited = []
    cycles = []
    c = Cube()
    c.execute(alg)
    def cycle(cube: Cube, face, i, j, lvl):
        target = SOLVED_STATE[face][i][j]
        if target in visited:
            cycles.append(lvl)
            visited.clear()
            return
        visited.append(cube.faces[face][i][j])

        for new_face in ["F", "R", "B", "L", "U", "D"]:
            for new_i in range(3):
                for new_j in range(3):
                    if target == cube.faces[new_face][new_i][new_j]:
                        cycle(cube, new_face, new_i, new_j, lvl+1)
                        return
    
    for face in ["F", "R", "B", "L", "U", "D"]:
        for i in range(3):
            for j in range(3):
                if SOLVED_STATE[face][i][j] != c.faces[face][i][j]:  
                    cycle(c, face, i, j, 1)
    
    order = reduce(math.lcm, cycles)
    return order

def brute_force(alg:str):
    c = Cube()
    order = 0
    while True:
        c.execute(alg)
        order+=1
        if c.faces == SOLVED_STATE:
            break
    return order