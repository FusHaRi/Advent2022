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

    # print(f"First ten: {rounds[:10]}")
    return rounds


def win_counter(rounds: list):
    global all
    my_wins, opponent_wins = 0, 0

    for i in rounds:
        if i[0] == rockOpponent:
            if i[1] == scissorsMy:
                opponent_wins += 1
            elif i[1] == paperMy:
                my_wins += 1

        if i[0] == paperOpponent:
            if i[1] == rockMy:
                opponent_wins += 1
            elif i[1] == scissorsMy:
                my_wins += 1

        if i[0] == scissorsOpponent:
            if i[1] == paperMy:
                opponent_wins += 1
            elif i[1] == rockMy:
                my_wins += 1

    print(f"My wins: {my_wins} \nOpponent wins: {opponent_wins}")
    return my_wins


def score_counter(rounds: list):
    global my_score
    global all

    for i in rounds:
        if i[0] == rockOpponent and i[1] == rockMy or i[0] == paperOpponent and i[1] == paperMy or i[0] == scissorsOpponent and i[1] == scissorsMy:
            my_score += 3
        if i[1] == rockMy:
            my_score += 1
        if i[1] == paperMy:
            my_score += 2
        if i[1] == scissorsMy:
            my_score += 3
    return


def main():
    global all
    showdown = rounds('strat_guide.txt')
    wins = win_counter(showdown)
    score_counter(showdown)

    print(f"My total score (Day 2 answer 1): {(wins*6) + my_score}")


main()
