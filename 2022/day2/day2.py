#!/usr/bin/env python3
"""Day2 of advent of code 2022.

A / X - Rock = 1 points
B / Y - Paper = 2 points
C / Z - Scissors = 3 points

Loss = 0
Draw = 3
Win = 6
"""

def sign_score(sign) -> int:
    """ Return the score for the sign given.

    A / X - Rock = 1 points
    B / Y - Paper = 2 points
    C / Z - Scissors = 3 points
    """
    if sign == 'A':
        return 1
    if sign == 'B':
        return 2
    return 3


def game_score(result) -> int:
    """Calculates the score from the given input."""
    if result == 'X':
        return 0
    if result == 'Y':
        return 3
    return 6


def cal_score(result, mine):
    """Calculate the total score for a game."""
    return sign_score(mine) + game_score(result)


def get_games() -> list:
    """returns a list of sets parsed from the input file."""
    # return [('A','Y'), ('B', 'X'), ('C', 'Z')]
    with open('input.txt', 'r', encoding='utf-8') as inp_f:
        for line in inp_f:
            [them, mine] = line.split()
            yield (them, mine)


def calc_mine(result, them):
    """Given the result, returns the needed sign."""
    if result == 'X': # Lose
        if them == 'A':
            return 'C'
        if them == 'B':
            return 'A'
        return 'B'

    if result == 'Z': # Win
        if them == 'A':
            return 'B'
        if them == 'B':
            return 'C'
        return 'A'

    return them # Draw


def main():
    """Main function."""
    total = 0
    games = get_games()
    for (them, result) in games:
        mine = calc_mine(result, them)
        print(f'result: {result}')
        print(f'mine: {mine}')
        print(f'them: {them}')
        score = cal_score(result, mine)
        print(f'score: {score}')
        print('----------------')
        total += score

    print(f'total: {total}')


if __name__ == '__main__':
    main()
