#!/usr/bin/env python3

import collections


class Rule:

    def __init__(self, s):
        self.base, self.production = s.split(' => ')

    def __str__(self):
        return '{} => {}'.format(self.base, self.production)

    def produce(self, state):
        if self.base == state:
            return True, self.production
        else:
            return False, None


class State:

    def __init__(self, line=''):
        self.cells = collections.defaultdict(int)
        if ':' in line:
            for i, c in enumerate(line.split(':')[1].strip()):
                self.cells[i] = 1 if c == '#' else 0
        else:
            for i, c in enumerate(iter(line)):
                self.cells[i] = 1 if c == '#' else 0

        self.min = 0
        self.max = len(self.cells)

    def set_cell(self, index, content):
        self.cells[index] = 1 if content == '#' else 0
        if content == '#':
            self.min = min(index, self.min)
            self.max = max(index, self.max)

    def __str__(self):
        cells = range(-5, 37)
        return ''.join([
            '#' if self.cells[k] == 1 else '.'
            for k in cells
            ]) + f'Min: {self.min}..{self.max}'

    def __iter__(self):
        return (
            (i, self.get_cells(i))
            for i in range(self.min-2, self.max+2)
            )

    def __len__(self):
        return self.max - self.min

    def get_cells(self, pos):
        return ''.join([
            '#' if self.cells[pos-2] == 1 else '.',
            '#' if self.cells[pos-1] == 1 else '.',
            '#' if self.cells[pos] == 1 else '.',
            '#' if self.cells[pos+1] == 1 else '.',
            '#' if self.cells[pos+2] == 1 else '.',
            ])


def read_initial_state(line):
    return State(line)


def read_rule(line):
    return Rule(line)


def read_input(filename):
    with open(filename, 'r') as fin:
        first_line = fin.readline()
        initial_state = read_initial_state(first_line)
        rules = []
        for line in fin:
            line = line.strip()
            if not line:
                continue
            rules.append(read_rule(line))
    return (initial_state, rules)


class Automat:

    def __init__(self, initial_state, rules):
        self.initial_state = initial_state
        self.current_state = initial_state
        self.rules = rules

    def apply_rules(self, cells):
        for rule in self.rules:
            applied, result = rule.produce(cells)
            if applied:
                return result
        return '.'

    def evolve(self):
        new_state = State()
        for i, cells in self.current_state:
            content = self.apply_rules(cells)
            new_state.set_cell(i, content)
        self.current_state = new_state
