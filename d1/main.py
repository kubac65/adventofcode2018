frequency = 0
history = set()
history.add(frequency)

# Read input file 
lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

continue_search = True
while continue_search:
    for l in lines:
        drift = int(l)
        frequency = frequency + drift
        if frequency in history: # yeah we have a match
            continue_search = False
            break

        history.add(frequency)
else:
    print('Frequency %d' % (frequency))