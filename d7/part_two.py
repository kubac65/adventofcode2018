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

# Part two
def funcname(self, parameter_list):
    pass


# add missing deps
for s in independent_steps:
    deps[s] = []

task_durations = {ch: idx+1+60 for (idx, ch) in enumerate(sorted(all_steps))}

workers = 5
ticks = 0
active_tasks = set()
complete_tasks = set()
assembing = True
while assembing:
    # check if any active tasks have completed to see if we can reuse the worker
    for a in list(active_tasks):
        if a[1] == ticks:
            # remove active task 
            active_tasks.remove(a)
            workers += 1
            complete_tasks.add(a[0])
            print('{} {} finished task {}'.format(ticks, workers, a[0]))
    if order:
        for _ in range(workers):
            if not workers:
                break
            for t in list(order):
                if complete_tasks.issuperset(deps[t]):
                    workers -= 1
                    completion_time = ticks + task_durations[t]
                    active_tasks.add((t, completion_time))
                    order.remove(t)
                    print('{} {} started task {}'.format(ticks, workers, t))
                    break


            # check if we can start some job
    if not order and len(complete_tasks) == len(all_steps):
        assembing = False

    ticks += 1