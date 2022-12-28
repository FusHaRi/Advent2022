# A = rock = X
# B = paper = Y
# C = scissors = Z
rockOpponent, paperOpponent, scissorsOpponent = 'A', 'B', 'C'
rockMy, paperMy, scissorsMy = 'X', 'Y', 'Z'
my_score, opponent_score = 0, 0


def rounds(input_file: str):
    global all
    rounds = []

    with open(input_file) as guide:
        for line in guide:
            rounds.append(line.split())

    return rounds


def win_lose_draw(rounds: list):
    global all
    global my_score
    lose, draw, win = 'X', 'Y', 'Z'

    for i in rounds:
        if i[1] == lose:
            if i[0] == rockOpponent:
                my_score += 3  # scissors loss
            elif i[0] == paperOpponent:
                my_score += 1  # rock loss
            elif i[0] == scissorsOpponent:
                my_score += 2  # paper loss

        elif i[1] == draw:
            my_score += 3
            if i[0] == rockOpponent:
                my_score += 1  # rock draw
            elif i[0] == paperOpponent:
                my_score += 2  # paper draw
            elif i[0] == scissorsOpponent:
                my_score += 3  # scissors draw

        elif i[1] == win:
            my_score += 6
            if i[0] == rockOpponent:
                my_score += 2  # paper win
            elif i[0] == paperOpponent:
                my_score += 3  # scissors win
            elif i[0] == scissorsOpponent:
                my_score += 1  # rock win

    print(f"My score (Day 2 answer 2): {my_score}")
    return my_score


def main():
    global all
    global my_score
    showdown = rounds('strat_guide.txt')
    win_lose_draw(showdown)


main()
