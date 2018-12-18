from collections import defaultdict, deque
import copy

lines = open('input.txt', 'r').readlines()

def to_bit_array(s, type):
    #return bitarray([c == '#' for c in s])
    return type(c == '#' for c in s)

initial_state = to_bit_array(lines[0].split()[2], deque)
transforms = defaultdict(bool, { to_bit_array(l.split()[0], tuple): l.split()[2] == '#' for l in lines[2:] })
print(initial_state)


def next_gen(previous_state, starting_idx):
    local_starting_idx = starting_idx -1
    leading = True
    next_state = deque()
    for _ in range(3):
        previous_state.appendleft(False)
        previous_state.append(False)
    # just a quick hack
    previous_state.append(False)

    window = deque([previous_state.popleft() for _ in range(5)])
    while previous_state:
        outcome = transforms[tuple(window)]
        if leading and outcome:
            leading = False
        elif leading:
            local_starting_idx += 1

        if not leading:
            next_state.append(outcome)

        if previous_state:
            window.popleft()
            window.append(previous_state.popleft())
        
    # prune leading False's
    stop = False
    while not stop:
        if next_state.pop():
            next_state.append(True)
            stop = True
    return next_state, local_starting_idx

def print_pots(pots):
    out = ''
    for i in pots:
        if i:
            out += '#'
        else:
            out += '.'
    print(out)

def sum_up(pots, starting_idx):
    pots_sum = 0
    for idx, plant_grows in enumerate(pots):
        if plant_grows:
            pots_sum += idx + starting_idx

    return pots_sum

pots = initial_state
starting_idx = 0
print_pots(pots)

seen_patterns = {}
target = 50000000000

iter = 0
while True:
    pots, idx = next_gen(pots, starting_idx)
    t_pots = tuple(pots)
    if t_pots in seen_patterns:
        #if target % iter == 0:
            p = iter - seen_patterns[t_pots][0]
            idx_diff = idx - seen_patterns[t_pots]

            remaining_repetitions = (target - iter) / p
            next_start_idx = int(idx + (remaining_repetitions * p))
            #idx_diff = idx - starting_idx

            #next_start_idx = idx + idx_diff * (target - iter)
            print(next_start_idx)
            print(sum_up(pots, next_start_idx))
            print_pots(pots)

            break
    else:
        seen_patterns[t_pots] = iter, starting_idx
        print(starting_idx)
        print(sum_up(pots, starting_idx))
        print_pots(pots)

    iter += 1
    starting_idx = idx

    #print(starting_idx)
    #print(sum_up(pots, starting_idx))
    #print_pots(pots)