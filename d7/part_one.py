import re
pattern = re.compile(r'Step\s([A-Z])[a-z\s]*([A-Z])')
deps = {}
all_steps = set()

def resolve_next(all_available, completed):
    resolved = None
    for s in all_available:
        if completed.issuperset(s[1]):
            resolved = s
            break
    all_available.remove(s)

    return resolved

with open('input.txt', 'r') as file:
    for l in file:
        # a must be finished before b can be started
        a, b = pattern.findall(l.strip())[0]
        all_steps.add(a)
        all_steps.add(b)

        if b not in deps:
            deps[b] = [a]
        else:
            deps[b].append(a)

# find steps without any dependencis 
independent_steps = sorted([s for s in all_steps if s not in deps])

unresolved_steps = [(key, value) for (key,value) in deps.items()]
# add othed independent steps to unresolved steps
if len(independent_steps) > 1:
    unresolved_steps.extend([(x, []) for x in independent_steps[1:]])
unresolved_steps.sort(key=lambda i: i[0])

order = list(independent_steps[0])
completed = set(independent_steps[0])



resolved = False
while not resolved:
    next_step = resolve_next(unresolved_steps, completed)
    completed.add(next_step[0])
    order.append(next_step[0])
    if not unresolved_steps:
        resolved = True

result = ''.join(order)
print(result)
