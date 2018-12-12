#!/usr/bin/env python3

from __future__ import print_function

from tools import Task, Scheduler, read_input

testing = not True
if testing:
    filename = 'sample.txt'
    num_workers = 2
    offset = 0
else:
    filename = 'input.txt'
    num_workers = 5
    offset = 60


all_tasks = set()
for task_0, task_1 in read_input(filename):
    all_tasks.add(task_0.name)
    all_tasks.add(task_1.name)

roots = Task.find_roots()
stack = list(sorted([t.name for t in roots]))
sch = Scheduler(num_workers, offset)
seen = set(stack)
for name in stack:
    task = Task.get(name)
    sch.add(task)
buff = []
counter = 0
while stack:
    counter += 1
    # print(stack)
    # print(sch)
    sch.run()
    for name in Task.registry:
        task = Task.get(name)
        if task.is_ready() and name not in seen:
            if name not in stack and name not in seen:
                stack.append(name)
                sch.add(task)
        if task.finished:
            seen.add(task.name)
            if name not in buff:
                buff.append(name)
            if name in stack:
                stack.remove(name)
solution = counter
print('Solution of part 2 is {}'.format(solution))
