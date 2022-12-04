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

def getOutcome(code):
    if code == 'X': return BattleOutcome.LOSS
    if code == 'Y': return BattleOutcome.DRAW
    return BattleOutcome.WIN

def backwardsBattle(opponent_move, outcome):
    if outcome == BattleOutcome.WIN:
        if opponent_move == Move.ROCK: return Move.PAPER
        if opponent_move == Move.PAPER: return Move.SCISSORS
        if opponent_move == Move.SCISSORS: return Move.ROCK

    if outcome == BattleOutcome.LOSS:
        if opponent_move == Move.ROCK: return Move.SCISSORS
        if opponent_move == Move.PAPER: return Move.ROCK
        if opponent_move == Move.SCISSORS: return Move.PAPER

    # Drawing means we always do the opp's move :P
    return opponent_move


def calculateScore(my_move, outcome):
    return int(my_move) + int(outcome)


dir_path = os.path.dirname(__file__)

input = open(dir_path + "\input.txt").read().strip('\n\n').split("\n")

total_score = 0

for line in input:
    opponent_move = getMove(line[0])
    outcome = getOutcome(line[2])
    my_move = backwardsBattle(opponent_move, outcome)
    total_score += calculateScore(my_move, outcome)

print(total_score)

# 11137 too low copy-pasted second part of backwardsBattle and didn't update the return vals
# 11186 *