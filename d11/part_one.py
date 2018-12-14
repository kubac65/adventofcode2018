input = 6303
grid_size = 300

def calc_power(x, y):
    rack_id = x + 10
    power = rack_id * y
    power = power + input
    power = power * rack_id
    # get the hundreds digit
    power = int(power / 100) % 10
    power = power - 5
    
    return(power)

grid = {(x,y): calc_power(x,y) for x in range(1, grid_size + 1) for y in range(1, grid_size + 1)}

coords = None
max_power = 0

for y in range(1, grid_size + 1):
    for x in range(1, grid_size + 1):
        power = 0
        if x+2 < grid_size + 1 and y+2 < grid_size + 1:
            for y_i in range(y, y+3):
                for x_i in range(x, x+3):
                    power += grid[x_i, y_i]

            if power > max_power:
                max_power = power
                coords = (x, y)
        else:
            break

print(coords, max_power)
