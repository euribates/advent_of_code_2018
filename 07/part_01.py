#!/usr/bin/env python3


import tools
import heapq

all_tasks = set()

for task_0, task_1 in tools.read_input('input.txt'):
    all_tasks.add(task_0.name)
    all_tasks.add(task_1.name)


roots = tools.Task.find_roots()
print('Roots are {}'.format(roots))
stack = [t.name for t in roots]
heapq.heapify(stack)
executed = set()
buff = []
while stack:
    print(stack)
    for nn in stack:
        print(tools.Task.get(nn))

    found_next = False
    descards = set([])
    while True:
        name = heapq.heappop(stack)
        task = tools.Task.get(name)
        if task.is_ready():
            break
        else:
            descards.add(name)
    for _ in descards:
        if _ not in stack:
            heapq.heappush(stack, _)
    print(task.name, end='')
    buff.append(task.name)
    task.finished = True
    for t in task:
        if not t.finished and t.name not in stack:
            heapq.heappush(stack, t.name)
print()
solution = ''.join(buff)
print(f'Solution of part 1 is {solution}')

