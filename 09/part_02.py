#!/usr/bin/env python3

from tools import play

test = False
if test:
    num_players = 9
    points = 27
else:
    num_players = 419
    points = 7216400

if __name__ == '__main__':
    scoreboard = play(num_players, points)
    winner = max(scoreboard, key=lambda k: scoreboard[k])
    solution = scoreboard[winner]
    print('Solution of part 2 is {}'.format(solution))
