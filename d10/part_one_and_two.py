from collections import deque, defaultdict
from math import sqrt, pow
from copy import copy
import re
import sys

lines = open('input.txt', 'r').readlines()
pattern = re.compile(r'(\-?\d*,\s*\-?\d*)')

coordinates = deque()
velocities = deque()

for l in lines:
    coords, velocity = pattern.findall(l)
    coords = tuple([int(c) for c in coords.split(', ')])
    velocity = tuple([int(v) for v in velocity.split(', ')])
    
    coordinates.append(coords)
    velocities.append(velocity)


keep_going = True
min_area = sys.maxsize
last_grid = None
seconds_passed = 0

while keep_going:
    seconds_passed += 1
    this_sec_grid = defaultdict(bool) 

    for _ in range(len(coordinates)):
        c = coordinates.popleft()
        v = velocities.popleft()

        new_c = (c[0] + v[0], c[1] + v[1])
        this_sec_grid[new_c] = True
        coordinates.append(new_c)
        velocities.append(v)

    # process one second
    x_min = min([c[0] for c in coordinates])
    x_max = max([c[0] for c in coordinates])

    y_min = min([c[1] for c in coordinates])
    y_max = max([c[1] for c in coordinates])

    area = sqrt(pow((x_min - x_max),2) + pow((y_min - y_max), 2))
    print(area)
    if area < min_area:
        min_area = area
        last_grid = copy(this_sec_grid)
    else:
        keep_going = False
        #print grid
        for y in range(y_min, y_max):
            row = ''
            skipped = True
            for x in range(x_min, x_max):
                if last_grid[(x, y)]:
                    row += '#'
                    skipped = False
                else: 
                    row += ' '

            if not skipped:
                print(row)

print(seconds_passed - 1)
