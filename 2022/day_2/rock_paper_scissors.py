

def calculate_score(input: list[str]) -> int:

    possible_games = {
        "A X" : 4,
        "A Y" : 8,
        "A Z" : 3,
        "B X" : 1,
        "B Y" : 5,
        "B Z" : 9,
        "C X" : 7,
        "C Y" : 2,
        "C Z" : 6
    }

    return sum(map(lambda x: possible_games[x], input))

#A Rock - 1
# B Paper - 2
# C Scissor - 3
# X - 0 loose
# Y - 3 draw
# Z - 6 win


def calculate_score_with_suggested_output(input: list[str]) -> int:

    possible_games = {
        "A X" : 3,
        "A Y" : 4,
        "A Z" : 8,
        "B X" : 1,
        "B Y" : 5,
        "B Z" : 9,
        "C X" : 2,
        "C Y" : 6,
        "C Z" : 7
    }

    return sum(map(lambda x: possible_games[x], input))
