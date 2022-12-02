ROCK = 1
PAPER = 2
SCISSOR = 3
WIN_LIST = [-2, 1]

weights = {}
weights['A'] = ROCK
weights['B'] = PAPER
weights['C'] = SCISSOR

weights['X'] = ROCK
weights['Y'] = PAPER
weights['Z'] = SCISSOR

f = open("input.txt", "r")
game_list = f.read().split("\n")


def score_game(game):
    score = 0
    competitor = game.split(' ')[0]
    you = game.split(' ')[1]

    if weights[competitor] == weights[you]:
        score += 3

    if (weights[you] - weights[competitor]) in WIN_LIST:
        score += 6

    return score + weights[you]

score = 0
for game in game_list:
    game_score = score_game(game)
    score += game_score

print(f'overall score: {score}')
