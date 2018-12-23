#!/usr/bin/env python3

from tools import Car


def test_move_car_right():
    car = Car(5, 5, '>')
    assert car.next() == (6, 5)


def test_move_car_left():
    car = Car(5, 5, '<')
    assert car.next() == (4, 5)


def test_move_car_up():
    car = Car(5, 5, '^')
    assert car.next() == (5, 4)


def test_move_car_down():
    car = Car(5, 5, 'v')
    assert car.next() == (5, 6)


def test_states_north():
    car = Car(5, 5, '^')
    assert car.state == 'N0'

def test_set_states_north_to_west():
    car = Car(5, 5, '^')
    assert car.orientation == Car.Orientation.NORTH
    assert car.count == 0
    assert car.state == 'N0'
    car.state = 'W1'
    assert car.orientation == Car.Orientation.WEST
    assert car.count == 1
    assert car.state == 'W1'


def test_set_states_east_to_south():
    car = Car(5, 5, '>')
    assert car.orientation == Car.Orientation.EAST
    assert car.count == 0
    assert car.state == 'E0'
    car.state = 'S1'
    assert car.orientation == Car.Orientation.SOUTH
    assert car.count == 1


def test_set_states_south_to_west():
    car = Car(5, 5, 'v')
    assert car.orientation == Car.Orientation.SOUTH
    assert car.count == 0
    assert car.state == 'S0'
    car.state = 'W1'
    assert car.orientation == Car.Orientation.WEST
    assert car.count == 1


def test_set_states_west_to_north():
    car = Car(5, 5, '<')
    assert car.orientation == Car.Orientation.WEST
    assert car.count == 0
    assert car.state == 'W0'
    car.state = 'N1'
    assert car.orientation == Car.Orientation.NORTH
    assert car.count == 1

    
    



