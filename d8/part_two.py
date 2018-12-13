from collections import deque

nums = None

with open('input.txt', 'r') as file:
    nums = deque([int(i) for i in file.read().strip().split()])

stk = []
processed_values_stk = []
ch = nums.popleft()
meta = nums.popleft()
# put initital node on the stack
stk.append((ch, meta, ch))

while stk:
    node = stk.pop()
    children_count, meta_count, orig_children_count = node # children count refers to the number of unprocessed children

    if not children_count:
        val = 0
        if not orig_children_count:
            for _ in range(meta_count):
                val += nums.popleft()
        else:
            child_vals = [processed_values_stk.pop() for _ in range(orig_children_count)]
            child_vals = child_vals[::-1] # reverse order
            for _ in range(meta_count):
                idx = nums.popleft()

                if idx == 0:
                    continue
                elif  idx > orig_children_count:
                    continue
                else:
                    val += child_vals[idx-1]


        processed_values_stk.append(val)
        # update the parent node to indicate that this one was completed
        if stk:
            parent_node = stk.pop()
            parent_node = (parent_node[0]-1, parent_node[1], parent_node[2])
            stk.append(parent_node)
    else:
        stk.append(node)
        # add new node onto the stack
        ch = nums.popleft()
        meta = nums.popleft()
        stk.append((ch, meta, ch))


print(val)