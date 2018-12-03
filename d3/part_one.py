def main():

    # A canvas is represented as a sparse-ish matrix.
    # Cell can have a value of 1 or 2, 1 meanign it's being cut out, 2 meaning it's an overlap
    canvas = {}

    claims = []
    overlaping = 0 
    with open('input.txt', 'r') as file:
        for line in file:
            claim_id, origin, dimension = process_line(line)
            claims.append((claim_id, origin, dimension))

            for x_coord in range(origin[0], origin[0] + dimension[0]):
                for y_coord in range(origin[1], origin[1]+ dimension[1]):
                    square = (x_coord, y_coord)

                    if square in canvas:
                        has_overlap = canvas[square] == 2

                        if has_overlap:
                            continue
                        else:
                            canvas[square] = 2 # mark the square to indicate that it has overlap
                            overlaping = overlaping + 1
                    else:
                        canvas[square] = 1

        print(overlaping)

def process_line(line):
    claim_id, _, origin, dimension = line.split(' ')
    origin = tuple(map(lambda x: int(x), origin[:-1].split(','))) # strip colon
    dimension = tuple(map(lambda x: int(x), dimension.split('x')))

    return claim_id, origin, dimension

if __name__ == '__main__':
    main()