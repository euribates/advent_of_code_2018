#!/usr/bin/env python3

from PIL import Image
from PIL import ImageDraw
import itertools
from enum import Enum

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY'
nums = '0123456789'
alphanums = alpha + nums


def get_names(first=alpha, rest=alphanums):
    for a, b in itertools.product(first, rest):
        yield '{}{}'.format(a, b)




class Cell:

    class Type(Enum):
        EMPTY = 0
        VERTICAL = 1
        HORIZONTAL = 2
        CURVE_RIGHT_UP = 3
        CURVE_LEFT_DOWN = 4
        INTERSECTION = 5

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        if s == ' ':
            self.type = Cell.Type.EMPTY
        elif s == '-' or s == '<' or s == '>':
            self.type = Cell.Type.HORIZONTAL
        elif s == '|' or s == '^' or s == 'v':
            self.type = Cell.Type.VERTICAL
        elif s == '/':
            self.type = Cell.Type.CURVE_RIGHT_UP
        elif s == '\\':
            self.type = Cell.Type.CURVE_LEFT_DOWN
        elif s == '+':
            self.type = Cell.Type.INTERSECTION
        else:
            raise ValueError(
                'Expected +, -, |, /, \\ or " ", not "{}"'.format(s)
            )

    def __str__(self):
        if self.type == Cell.Type.EMPTY:
            return ' '
        elif self.type == Cell.Type.HORIZONTAL:
            return '-'
        elif self.type == Cell.Type.VERTICAL:
            return '|'
        elif self.type == Cell.Type.CURVE_RIGHT_UP:
            return '/'
        elif self.type == Cell.Type.CURVE_LEFT_DOWN:
            return '\\'
        elif self.type == Cell.Type.INTERSECTION:
            return '+'
        else:
            raise ValueError('Unknown cell type {}'.format(self.type))


class ImageMap:

    def __init__(self, state_map):
        self.state_map = state_map
        self.width = state_map.width * 5
        self.height = state_map.height * 5
        self.image = Image.new('RGB', (self.width, self.height))

    def up_type(self, cell):
        x, y = cell.x, cell.y
        # print('up_type({}, {})'.format(x, y))
        if y <= 0:
            return Cell.Type.EMPTY
        return self.state_map[(x, y-1)].type

    def down_type(self, cell):
        x, y = cell.x, cell.y
        if y >= self.state_map.height-1:
            return Cell.Type.EMPTY
        return self.state_map[(x, y+1)].type

    def left_type(self, cell):
        x, y = cell.x, cell.y
        if x <= 0:
            return Cell.Type.EMPTY
        return self.state_map[(x-1, y)].type

    def right_type(self, cell):
        x, y = cell.x, cell.y
        if x >= self.state_map.width-1:
            return Cell.Type.EMPTY
        return self.state_map[(x+1, y)].type

    def draw(self):
        for y in range(self.state_map.height):
            for x in range(self.state_map.width):
                cell = self.state_map[(x, y)]
                self.draw_cell(cell)
        for car in self.state_map.cars:
            self.draw_car(car)

    def save(self, filename):
        self.image.save(filename)


    def draw_car(self, car):
        draw = ImageDraw.Draw(self.image)
        assert 0 <= car.count < 3
        if car.count == 0:
            color = (255, 22, 22)
        elif car.count == 1:
            color = (255, 129, 6)
        elif car.count == 2:
            color = (255, 195, 177)

        x, y = car.x * 5 + 3, car.y * 5 + 3
        if car.orientation == Car.Orientation.NORTH:
             draw.polygon(
                [(x-2, y+1), (x, y-1), (x+2, y+1)],
                fill=color
                )
        if car.orientation == Car.Orientation.EAST:
             draw.polygon(
                [(x, y-2), (x+2, y), (x, y+2)],
                fill=color
                )
        if car.orientation == Car.Orientation.SOUTH:
             draw.polygon(
                [(x-2, y-1), (x, y+1), (x+2, y-1)],
                fill=color
                )
        if car.orientation == Car.Orientation.WEST:
             draw.polygon(
                [(x, y-2), (x, y+2), (x-2, y)],
                fill=color
                )


    def draw_cell(self, cell):
        x, y = cell.x * 5 + 3, cell.y * 5 + 3
        draw = ImageDraw.Draw(self.image)
        if cell.type == Cell.Type.HORIZONTAL:
            draw.line((x-3, y, x+2, y), fill=(33, 255, 33))
        elif cell.type == Cell.Type.VERTICAL:
            draw.line((x, y-3, x, y+2), fill=(33, 255, 33))
        elif cell.type == Cell.Type.CURVE_RIGHT_UP:
            flag = all([
                self.down_type(cell) in (Cell.Type.VERTICAL, Cell.Type.INTERSECTION),
                self.right_type(cell) in (Cell.Type.HORIZONTAL, Cell.Type.INTERSECTION)
                ])
            if flag:
                draw.line((x, y+2, x+2, y), fill=(33, 255, 33))
            else:
                draw.line((x-2, y, x, y-2), fill=(33, 255, 33))
        elif cell.type == Cell.Type.CURVE_LEFT_DOWN:
            flag = all([
                self.up_type(cell) in (Cell.Type.VERTICAL, Cell.Type.INTERSECTION),
                self.right_type(cell) in (Cell.Type.HORIZONTAL, Cell.Type.INTERSECTION),
                ])
            if flag:
                draw.line((x, y-2, x+2, y), fill=(33, 255, 33))
            else:
                draw.line((x-2, y, x, y+2), fill=(33, 255, 33))
        elif cell.type == Cell.Type.INTERSECTION:
            draw.line((x-3, y, x+2, y), fill=(33, 255, 33))
            draw.line((x, y-3, x, y+2), fill=(33, 255, 33))


class StateMap(dict):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cars = []

    def __str__(self):
        buff = []
        for y in range(self.height):
            for x in range(self.width):
                for car in self.cars:
                    if car.x == x and car.y == y:
                        buff.append(str(car))
                        break
                else:
                    cell = self[(x, y)]
                    buff.append(str(cell))
            buff.append('\n')
        return ''.join(buff)

    def tick(self):
        global StatesMechine
        self.crashed = set()
        for car in self.get_cars():
            next_cell = (new_x, new_y) = car.next()
            cell_type = self[next_cell].type
            state = car.state
            assert (state, cell_type) in StatesMachine
            car.state = StatesMachine[(state, cell_type)]
            car.x = new_x
            car.y = new_y
            if self.is_crash():
                self.crashed = self.find_crashed()

    def is_crash(self):
        for a, b in itertools.combinations(self.cars, 2):
            if a == b:
                return True
        return False

    def find_crashed(self):
        result = set()
        for a, b in itertools.combinations(self.cars, 2):
            if a == b:
                result.add(a)
                result.add(b)
        return result

    def get_cars(self):
        return sorted(self.cars, key=lambda c: (c.y, c.x))


class Car:

    names = get_names()

    class Orientation(Enum):

        NORTH = 1
        EAST = 2
        SOUTH = 3
        WEST = 4

    def __init__(self, x, y, char):
        self.name = next(Car.names)
        self.x = x
        self.y = y
        self.count = 0
        if char == '^':
            self.orientation = Car.Orientation.NORTH
        elif char == '>':
            self.orientation = Car.Orientation.EAST
        elif char == 'v':
            self.orientation = Car.Orientation.SOUTH
        elif char == '<':
            self.orientation = Car.Orientation.WEST

    def __hash__(self):
        return ord(self.name[0]) * 256 + ord(self.name[1])

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @property
    def state(self):
        if self.orientation == Car.Orientation.NORTH:
            return 'N{}'.format(self.count)
        elif self.orientation == Car.Orientation.EAST:
            return 'E{}'.format(self.count)
        elif self.orientation == Car.Orientation.SOUTH:
            return 'S{}'.format(self.count)
        elif self.orientation == Car.Orientation.WEST:
            return 'W{}'.format(self.count)
        else:
            raise ValueError('Bad orientation {}'.format(self.orientation))

    @state.setter
    def state(self, new_state):
        orientation = new_state[0]
        if orientation not in 'NESW':
            raise ValueError('Bad orientation {}'.format(self.orientation))
        if orientation == 'N':
            self.orientation = Car.Orientation.NORTH
        elif orientation == 'E':
            self.orientation = Car.Orientation.EAST
        elif orientation == 'S':
            self.orientation = Car.Orientation.SOUTH
        else:
            self.orientation = Car.Orientation.WEST
        count = new_state[1]
        if count not in '012':
            raise ValueError('Bad orientation {}'.format(self.orientation))
        self.count = int(count)

    def __str__(self):
        buff = ['\033[92m']
        if self.orientation == Car.Orientation.NORTH:
            buff.append('^')
        elif self.orientation == Car.Orientation.EAST:
            buff.append('>')
        elif self.orientation == Car.Orientation.SOUTH:
            buff.append('v')
        elif self.orientation == Car.Orientation.WEST:
            buff.append('<')
        buff.append('\033[0m')
        return ''.join(buff)

    def __repr__(self):
        return 'Car {} at {}x{} facing {} count is {}'.format(
            self.name, 
            self.x,
            self.y,
            self.orientation,
            self.count,
            )

    def next(self):
        if self.orientation == Car.Orientation.NORTH:
            return (self.x, self.y-1)
        elif self.orientation == Car.Orientation.SOUTH:
            return (self.x, self.y+1)
        elif self.orientation == Car.Orientation.EAST:
            return (self.x+1, self.y)
        elif self.orientation == Car.Orientation.WEST:
            return (self.x-1, self.y)


def read_input(filename='input.txt'):
    with open(filename) as fh:
        lines = fh.readlines()
        width = len(lines[0]) - 1
        height = len(lines)
        state = StateMap(width, height)
        for y, line in enumerate(lines):
            for x, c in enumerate(line[0:-1]):
                state[(x, y)] = Cell(x, y, c)
                if c in '^>v<':
                    state.cars.append(Car(x, y, c))
    return state



StatesMachine = {
    # North
    ('N0', Cell.Type.VERTICAL): 'N0',
    ('N1', Cell.Type.VERTICAL): 'N1',
    ('N2', Cell.Type.VERTICAL): 'N2',
    ('N0', Cell.Type.CURVE_RIGHT_UP): 'E0',
    ('N1', Cell.Type.CURVE_RIGHT_UP): 'E1',
    ('N2', Cell.Type.CURVE_RIGHT_UP): 'E2',
    ('N0', Cell.Type.CURVE_LEFT_DOWN): 'W0',
    ('N1', Cell.Type.CURVE_LEFT_DOWN): 'W1',
    ('N2', Cell.Type.CURVE_LEFT_DOWN): 'W2',
    ('N0', Cell.Type.INTERSECTION): 'W1',
    ('N1', Cell.Type.INTERSECTION): 'N2',
    ('N2', Cell.Type.INTERSECTION): 'E0',

    # East 
    ('E0', Cell.Type.HORIZONTAL): 'E0',
    ('E1', Cell.Type.HORIZONTAL): 'E1',
    ('E2', Cell.Type.HORIZONTAL): 'E2',
    ('E0', Cell.Type.CURVE_RIGHT_UP): 'N0',
    ('E1', Cell.Type.CURVE_RIGHT_UP): 'N1',
    ('E2', Cell.Type.CURVE_RIGHT_UP): 'N2',
    ('E0', Cell.Type.CURVE_LEFT_DOWN): 'S0',
    ('E1', Cell.Type.CURVE_LEFT_DOWN): 'S1',
    ('E2', Cell.Type.CURVE_LEFT_DOWN): 'S2',
    ('E0', Cell.Type.INTERSECTION): 'N1',
    ('E1', Cell.Type.INTERSECTION): 'E2',
    ('E2', Cell.Type.INTERSECTION): 'S0',

    # South
    ('S0', Cell.Type.VERTICAL): 'S0',
    ('S1', Cell.Type.VERTICAL): 'S1',
    ('S2', Cell.Type.VERTICAL): 'S2',
    ('S0', Cell.Type.CURVE_RIGHT_UP): 'W0',
    ('S1', Cell.Type.CURVE_RIGHT_UP): 'W1',
    ('S2', Cell.Type.CURVE_RIGHT_UP): 'W2',
    ('S0', Cell.Type.CURVE_LEFT_DOWN): 'E0',
    ('S1', Cell.Type.CURVE_LEFT_DOWN): 'E1',
    ('S2', Cell.Type.CURVE_LEFT_DOWN): 'E2',
    ('S0', Cell.Type.INTERSECTION): 'E1',
    ('S1', Cell.Type.INTERSECTION): 'S2',
    ('S2', Cell.Type.INTERSECTION): 'W0',

    # West 
    ('W0', Cell.Type.HORIZONTAL): 'W0',
    ('W1', Cell.Type.HORIZONTAL): 'W1',
    ('W2', Cell.Type.HORIZONTAL): 'W2',
    ('W0', Cell.Type.CURVE_RIGHT_UP): 'S0',
    ('W1', Cell.Type.CURVE_RIGHT_UP): 'S1',
    ('W2', Cell.Type.CURVE_RIGHT_UP): 'S2',
    ('W0', Cell.Type.CURVE_LEFT_DOWN): 'N0',
    ('W1', Cell.Type.CURVE_LEFT_DOWN): 'N1',
    ('W2', Cell.Type.CURVE_LEFT_DOWN): 'N2',
    ('W0', Cell.Type.INTERSECTION): 'S1',
    ('W1', Cell.Type.INTERSECTION): 'W2',
    ('W2', Cell.Type.INTERSECTION): 'N0',

    }

def draw_frame(state, frame):
    output = 'frames/frame_{:04d}.png'
    img = ImageMap(state)
    img.draw()
    img.save(output.format(frame))
