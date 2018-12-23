#!/usr/bin/env python3

import pytest

from tools import Car
from tools import StateMap
from tools import Cell


@pytest.fixture
def car_up():
    car = Car(5, 1, '^')
    state = StateMap(10, 10)
    state.cars = [car]
    state[(5,0)] = Cell(5, 1, '+')
    state[(5,1)] = Cell(5, 1, '|')
    return state, car

def test_state_machine_up_cross_zero(car_up):
    state, car = car_up
    state.tick()
    assert car.count == 1
    assert car.orientation == Car.Orientation.WEST
    assert car.x == 5
    assert car.y == 0


def test_state_machine_up_cross_one(car_up):
    state, car = car_up
    car.count = 1
    state.tick()
    assert car.count == 2
    assert car.orientation == Car.Orientation.NORTH
    assert car.x == 5
    assert car.y == 0


def test_state_machine_up_cross_two(car_up):
    state, car = car_up
    car.count = 2
    state.tick()
    assert car.count == 0
    assert car.orientation == Car.Orientation.EAST
    assert car.x == 5
    assert car.y == 0


@pytest.fixture
def car_down():
    car = Car(5, 0, 'v')
    state = StateMap(10, 10)
    state.cars = [car]
    state[(5,0)] = Cell(5, 0, '|')
    state[(5,1)] = Cell(5, 1, '+')
    return state, car


def test_state_machine_down_cross_zero(car_down):
    state, car = car_down
    state.tick()
    assert car.count == 1
    assert car.orientation == Car.Orientation.EAST
    assert car.x == 5
    assert car.y == 1


def test_state_machine_down_cross_one(car_down):
    state, car = car_down
    car.count = 1
    state.tick()
    assert car.orientation == Car.Orientation.SOUTH
    assert car.count == 2
    assert car.x == 5
    assert car.y == 1


def test_state_machine_down_cross_two(car_down):
    state, car = car_down
    car.count = 2
    state.tick()
    assert car.orientation == Car.Orientation.WEST
    assert car.count == 0
    assert car.x == 5
    assert car.y == 1


@pytest.fixture
def car_right():
    car = Car(5, 5, '>')
    state = StateMap(10, 10)
    state.cars = [car]
    state[(5,5)] = Cell(5, 5, '-')
    state[(6,5)] = Cell(6, 5, '+')
    return state, car


def test_state_machine_right_cross_zero(car_right):
    state, car = car_right
    state.tick()
    assert car.count == 1
    assert car.orientation == Car.Orientation.NORTH
    assert car.x == 6
    assert car.y == 5


def test_state_machine_right_cross_one(car_right):
    state, car = car_right
    car.count = 1
    state.tick()
    assert car.count == 2
    assert car.orientation == Car.Orientation.EAST
    assert car.x == 6
    assert car.y == 5


def test_state_machine_right_cross_two(car_right):
    state, car = car_right
    car.count = 2
    state.tick()
    assert car.count == 0
    assert car.orientation == Car.Orientation.SOUTH
    assert car.x == 6
    assert car.y == 5


@pytest.fixture
def car_left():
    car = Car(5, 5, '<')
    state = StateMap(10, 10)
    state.cars = [car]
    state[(5,5)] = Cell(5, 5, '-')
    state[(4,5)] = Cell(6, 5, '+')
    return state, car


def test_state_machine_lwft_cross_zero(car_left):
    state, car = car_left
    state.tick()
    assert car.count == 1
    assert car.orientation == Car.Orientation.SOUTH
    assert car.x == 4
    assert car.y == 5


def test_state_machine_lwft_cross_one(car_left):
    state, car = car_left
    car.count = 1
    state.tick()
    assert car.count == 2
    assert car.orientation == Car.Orientation.WEST
    assert car.x == 4
    assert car.y == 5


def test_state_machine_lwft_cross_two(car_left):
    state, car = car_left
    car.count = 2
    state.tick()
    assert car.count == 0
    assert car.orientation == Car.Orientation.NORTH
    assert car.x == 4
    assert car.y == 5



