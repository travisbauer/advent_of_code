ROCK_VALUE = 1
PAPER_VALUE = 2
SCISSOR_VALUE = 3
ROCK = 'A'
PAPER = 'B'
SCISSOR = 'C'
LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

weights = {}
weights[ROCK] = ROCK_VALUE
weights[PAPER] = PAPER_VALUE
weights[SCISSOR] = SCISSOR_VALUE

win_dict = {}
win_dict[LOSE] = {}
win_dict[DRAW] = {}
win_dict[WIN] = {}

win_dict[LOSE][ROCK] = SCISSOR
win_dict[LOSE][PAPER] = ROCK
win_dict[LOSE][SCISSOR] = PAPER

win_dict[DRAW][ROCK] = ROCK
win_dict[DRAW][PAPER] = PAPER
win_dict[DRAW][SCISSOR] = SCISSOR

win_dict[WIN][ROCK] = PAPER
win_dict[WIN][PAPER] = SCISSOR
win_dict[WIN][SCISSOR] = ROCK

f = open("input.txt", "r")
game_list = f.read().split("\n")

def score_game(game):
    score = 0
    competitor = game.split(' ')[0]
    win = game.split(' ')[1]
    you = win_dict[win][competitor]

    if win == 'Y':
        score += 3
    elif win == 'Z':
        score += 6

    return score + weights[you]

score = 0
for game in game_list:
    game_score = score_game(game)
    score += game_score

print(f'overall score: {score}')
