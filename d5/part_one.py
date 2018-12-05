def main():
    polymer = ''
    with open('input.txt', 'r') as file:
        polymer = file.readlines()[0].strip()

    still_reacting = True
    cycle = 0
    while still_reacting:
        polymer, still_reacting = react(polymer)
        cycle += 1
        print(cycle, len(polymer))


    # print(len(resulted_polymer))

def react(polymer):
    new_polymer = ''
    cursor = 0
    has_reacted = False

    while cursor < len(polymer):
        # if last element then there is nothing to react with
        if cursor == len(polymer) - 1:
            new_polymer += polymer[cursor]
            cursor += 1
        elif polymer[cursor] != polymer[cursor +1] and polymer[cursor].lower() == polymer[cursor+1].lower():
            # Skip both of the units
            has_reacted = True
            cursor += 2
        else:
            # add unit to new polymer
            new_polymer += polymer[cursor]
            cursor += 1

    return (new_polymer, has_reacted)




if __name__ == '__main__':
    main()