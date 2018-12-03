def main():
    # Each square on the canvas contains the reference to all claims that overlap it
    canvas = {}
    # Dictionary below holds ids of the claims and boolean flags indicating whether they overlap or not
    claims_is_overlapping = {}

    with open('input.txt', 'r') as file:
        for line in file:
            claim_id, origin, dimension = process_line(line)
            claims_is_overlapping[claim_id] = False

            for x_coord in range(origin[0], origin[0] + dimension[0]):
                for y_coord in range(origin[1], origin[1]+ dimension[1]):
                    square = (x_coord, y_coord)

                    if square in canvas:
                        canvas[square].append(claim_id)
                        # Mark claims for the square overlapping
                        for c in canvas[square]:
                            claims_is_overlapping[c] = True
                    else:
                        canvas[square] = [claim_id]


        for i in [i for i in claims_is_overlapping.items() if i[1] == False]:
            print(i) # there should be only one

def process_line(line):
    claim_id, _, origin, dimension = line.split(' ')
    origin = tuple(map(lambda x: int(x), origin[:-1].split(','))) # strip colon
    dimension = tuple(map(lambda x: int(x), dimension.split('x')))

    return claim_id, origin, dimension

if __name__ == '__main__':
    main()