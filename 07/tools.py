#!/usr/bin/env python3

import re


class Task:

    registry = {}

    def __init__(self, name):
        self.name = name
        self.requires = set([])
        self.follows = set([])
        self.finished = False

    @classmethod
    def reset(cls):
        cls.registry = {}

    @classmethod
    def find_roots(cls):
        result = []
        for name in cls.registry:
            task = cls.get(name)
            if not task.requires:
                result.append(task)
        return result

    @classmethod
    def get(cls, name):
        if name not in cls.registry:
            new_task = Task(name)
            Task.registry[name] = new_task
        return Task.registry[name]

    def is_ready(self):
        return all([
            t.finished
            for t in self.requires
            ])

    def __repr__(self):
        preconditions = ', '.join([t.name for t in self.requires])
        next_tasks = ', '.join([t.name for t in self.follows])
        if not preconditions:
            return '{} -> [{}]'.format(
                self.name,
                next_tasks,
                )
        elif not next_tasks:
            return '[{}] -> {}'.format(
                preconditions,
                self.name,
                )
        else:
            return '[{}] -> {} -> [{}]'.format(
                preconditions,
                self.name,
                next_tasks,
                )

    def __iter__(self):
        return (
            t
            for t in sorted(self.follows, key=lambda t: t.name)
            )


class Worker:

    def __init__(self, offset=60):
        self.offset = offset
        self.free = True

    def run(self, task):
        self.task = task
        self.free = False
        self.clock = 0
        self.count = self.offset + ord(task.name) - 65

    def click(self):
        if self.free:
            return
        self.clock += 1
        if self.clock >= self.count:
            self.task.finished = True
            self.free = True


class Scheduler:

    def __init__(self, num_workers=2, offset=60):
        self.workers = [
            Worker(offset)
            for _ in range(num_workers)
            ]
        self.queue = []

    def __repr__(self):
        buff = []
        buff.append('--[Scheduler]-------------------')
        buff.append('Queue: {}'.format(
            ', '.join(self.queue) if self.queue else 'empty'
            ))
        buff.append('Workers: {}'.format(len(self.workers)))
        for i, w in enumerate(self.workers):
            buff.append(' - worker {} is {}'.format(
                i,
                'free' if w.free else 'working on task {}'.format(w.task.name),
                ))
        buff.append('--[End Scheduler]---------------')
        return '\n'.join(buff)

    def add(self, task):
        self.queue.append(task.name)

    def available_workers(self):
        return [w for w in self.workers if w.free]

    def click(self):
        for worker in self.workers:
            worker.click()

    def run(self):
        self.click()
        for worker in self.available_workers():
            names = sorted(self.queue)
            for name in names:
                task = Task.get(name)
                if task.is_ready():
                    worker.run(task)
                    self.queue.remove(name)
                    break


def parse(line):
    m = parse.pat.match(line)
    t0 = Task.get(m.group(1))
    t1 = Task.get(m.group(2))
    t0.follows.add(t1)
    t1.requires.add(t0)
    return t0, t1


parse.pat = re.compile('Step (.) must be finished before step (.) can begin.')


def read_input(filename='input.txt', transform=parse):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return (transform(line.strip()) for line in lines)
