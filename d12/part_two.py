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

i = 0
continue_searching = True
prev_sum = 0

while continue_searching:
    pots, starting_idx = next_gen(pots, starting_idx)
    curr_sum = sum_up(pots, starting_idx)
    t_pots = tuple(pots)
    i += 1
    if t_pots in seen_patterns:
        final_sum = curr_sum + (target - i) * (curr_sum - prev_sum)
        print('final sum: ' + str(final_sum))
        continue_searching = False
    else:
        print('idx:' + str(starting_idx))
        print('iteration:' + str(i))
        print('sum:' + str(curr_sum))
        print_pots(pots)
        seen_patterns[t_pots] = i, starting_idx
        prev_sum = curr_sum