import os
input = 6303
grid_size = 300

#input = 1845
#grid_size = 5

def calc_power(x, y):
    rack_id = x + 10
    power = rack_id * y
    power = power + input
    power = power * rack_id
    # get the hundreds digit
    power = int(power / 100) % 10
    power = power - 5
    
    return(power)

def print_grid(grid):
    rows = []

    for y in range(1, grid_size+1):
        row = ''
        for x in range(1, grid_size+1):
            cell = str(grid[x,y]).rjust(2)  + ' ' 
            row += cell

        row += os.linesep
        print(row)
        rows.append(row)

    return rows

grid = {(x,y): calc_power(x,y) for x in range(1, grid_size + 1) for y in range(1, grid_size + 1)}

rows = print_grid(grid)
with open('out.txt', 'w') as file:
    file.writelines(rows)

coords = None
max_power = -10
max_size = 0

for y in range(1, grid_size + 1):
    for x in range(1, grid_size + 1):
        power = 0
        max_local_size = grid_size + 1 - max([x, y])

        for s in range(1, max_local_size + 1):
            # read powers of x row and y column
            if s == 1:
                power = grid[x,y]

            else:
                power += sum([grid[l_x, y+s-1] for l_x in range(x, x+s-1)])
                power += sum([grid[x+s-1, l_y] for l_y in range(y, y+s-1)])
                power += grid[x+s-1, y+s-1]

            if power > max_power:
                max_power = power
                coords = (x, y)
                max_size = s

print(coords, max_size, max_power)
