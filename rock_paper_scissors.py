import random


def play():
    user = input("'r' for rock, 'p' for paper 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return "player wins"

    return "opponent wins"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
            or (player == 's' and opponent == 'p'):
        return True


def is_loss(player, opponent):
    if (player == 's' and opponent == 'r') or (player == 'r' and opponent == 'p') \
            or (player == 'p' and opponent == 's'):
        return False


print(play())
