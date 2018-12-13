player_count = 458
last_marble = 71307

# player_count = 9
# last_marble = 25

multiple_of = 23
offset = 7 #also take marble, located 7 marbles to the left

high_scores = [0 for _ in range(player_count)]

marbles = [0]
current_marble = 1
current_marble_idx = 0

while current_marble < last_marble:
    for pl in range(player_count):
        new_marble_idx = current_marble_idx + 2
        if new_marble_idx > len(marbles):
            new_marble_idx = 1

        if current_marble % multiple_of == 0:
            additional_marble_idx = current_marble_idx - offset
            if additional_marble_idx < 0:
                additional_marble_idx = len(marbles) + additional_marble_idx

            m = marbles.pop(additional_marble_idx)
            current_marble_idx = additional_marble_idx
            high_scores[pl] += current_marble + m
        else:
            marbles.insert(new_marble_idx, current_marble)
            current_marble_idx = new_marble_idx

        current_marble +=1
        if current_marble == last_marble:
            break
        # print(marbles)

print(max(high_scores))

