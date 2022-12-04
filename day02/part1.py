import os
from enum import IntEnum

class Move(IntEnum): 
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class BattleOutcome(IntEnum):
    WIN = 6
    LOSS = 0
    DRAW = 3

def getMove(code):
    if code == 'A' or code == "X":
        return Move.ROCK
    elif code == 'B' or code == "Y":
        return Move.PAPER
    return Move.SCISSORS


def battle(opponent_move, my_move):
    if ((opponent_move == Move.ROCK and my_move == Move.PAPER) or
       (opponent_move == Move.PAPER and my_move == Move.SCISSORS) or 
       (opponent_move == Move.SCISSORS and my_move == Move.ROCK)):

       return BattleOutcome.WIN

    if ((opponent_move == Move.ROCK and my_move == Move.SCISSORS) or
       (opponent_move == Move.PAPER and my_move == Move.ROCK) or 
       (opponent_move == Move.SCISSORS and my_move == Move.PAPER)):

       return BattleOutcome.LOSS

    return BattleOutcome.DRAW

def calculateScore(my_move, outcome):
    return int(my_move) + int(outcome)


dir_path = os.path.dirname(__file__)

input = open(dir_path + "\input.txt").read().strip('\n\n').split("\n")

total_score = 0

for line in input:
    opponent_move = getMove(line[0])
    my_move = getMove(line[2])
    outcome = battle(opponent_move, my_move)
    total_score += calculateScore(my_move, outcome)

print(total_score)

# 11906 *


    


    