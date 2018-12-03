def main():
    lines = []

    with open('input.txt' ,'r') as f:
        lines = f.readlines()

    tuples = 0
    triples = 0

    for line in lines:
        has_tuple, has_triple = process_line(line)

        if has_tuple:
            tuples = tuples + 1
        
        if has_triple:
            triples = triples + 1

    # calculate result

    result = tuples * triples
    print("Result %d" % (result))

def process_line(line):
    counts = {}

    for ch in line:
        if ch not in counts:
            counts[ch] = 1
        else:
            counts[ch] = counts[ch] + 1

    has_tuple = 2 in counts.values()
    has_triple = 3 in counts.values()

    return (has_tuple, has_triple)

if __name__ == '__main__':
    main()