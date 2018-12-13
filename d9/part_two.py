from collections import deque
player_count = 458
last_marble = 7130700

# player_count = 10
# last_marble = 1618

multiple_of = 23
offset = 7 #also take marble, located 7 marbles to the left

high_scores = [0 for _ in range(player_count)]

marbles = deque([0])
current_marble = 1

while current_marble < last_marble:
    for pl in range(player_count):
        # rotate
        marbles.append(marbles.popleft())

        if current_marble % multiple_of == 0:
            for _ in range(offset+1):
                marbles.appendleft(marbles.pop())
            m = marbles.pop()
            marbles.append(marbles.popleft())
            high_scores[pl] += current_marble + m
            # marbles.append(marbles.popleft())
        else:
            marbles.append(current_marble)

        if current_marble == last_marble:
            break

        current_marble +=1
        # print(marbles)

print(max(high_scores))

