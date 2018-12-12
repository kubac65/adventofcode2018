from collections import deque

header_size = 2
nums = None

with open('input.txt', 'r') as file:
    nums = deque([int(i) for i in file.read().strip().split()])
print(nums)

sum = 0
# put initital node on the stack
stk = []
stk.append((nums.popleft(), nums.popleft()))

while stk:
    node = stk.pop()
    children_count, meta_count = node

    if not children_count:
        for _ in range(meta_count):
            sum += nums.popleft()
        # update the parent node to say that this one was completed
        if stk:
            parent_node = stk.pop()
            parent_node = (parent_node[0]-1, parent_node[1])
            stk.append(parent_node)
    else:
        stk.append(node)
        # add new node onto the stack
        stk.append((nums.popleft(), nums.popleft()))


print(sum)




















#meta_sum = 0
#visited_nodes = 0
#def process_node(nums):
#    node_lenght = 0
#    if nums:
#        global meta_sum
#        global visited_nodes
#        child_count = nums[0]
#        meta_count = nums[1]

#        node_lenght = 2 + meta_count

#        if not child_count:
#            meta_sum += sum(nums[2: 2+meta_count])

#        else:
#            sub_nums = None
#            if meta_count:
#                meta_sum += sum(nums[-meta_count:])
#                # need to find all child nodes
#                sub_nums = nums[2:-meta_count]
#            else:
#                sub_nums = nums[2:]
#            # above may contain more than one node
#            # it needs to be split 
        
#            split = 0
#            for c in range(child_count):
#                s = sub_nums[split:]
#                if s:
#                    split = process_node(s)
#                    node_lenght += split
#                else:
#                    print(sub_nums)
#                    break
            
#        visited_nodes +=1
#        print(meta_sum)

#    return node_lenght

#process_node(nums)

#print(meta_sum)

