from collections import Counter
coordinates = [tuple(map(int, l.strip().split(', '))) for l in open('input.txt', 'r').readlines()]
labels = {c:i for i, c in enumerate(coordinates)}

x_max = max([c[0] for c in coordinates])
x_min = min([c[0] for c in coordinates])
y_max = max([c[1] for c in coordinates])
y_min = min([c[1] for c in coordinates])


def distance(c1, c2):
    d = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
    return d;

grid = {}
infinite_labels = set()

for x in range(x_min, x_max + 1):
    for y in range(y_min, y_max + 1):

        min_distance = 1e5
        closest_label = None
        shared = False

        for c in coordinates:
            d = distance(c, (x,y))
            if d < min_distance:
                min_distance = d
                closest_label = labels[c]
                shared = False

            elif d == min_distance:
                shared = True

        if not shared:
            grid[x,y] = closest_label

            if x == x_min or x == x_max or y ==y_min or y == y_max:
                infinite_labels.add(closest_label)


areas = Counter([gv for gv in grid.values() if gv not in infinite_labels])
print(max(areas))
