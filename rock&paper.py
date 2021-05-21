import random

def play():
    try:
        user = int(input("What's your choice? \n (1) Rock \n (2) Paper \n (3) Scissor \n" ))
    except ValueError as ve:
        print(ve)
    computer = random.randint(1, 3)
    print("Your opponent chose " + str(computer))

    if user == computer:
        return 'Tie!'

    """
    (1)Rock
    (2)Paper
    (3)Scissor
    1 > 3, 2 > 1, 3 > 2 
    """
    if win(user, computer):
        return 'You Won!'

    return 'You lost!'

def win(player1, player2):
    """
    (1)Rock
    (2)Paper
    (3)Scissor
    1 > 3, 2 > 1, 3 > 2 
    """
    if(player1 == 1 and player2 == 3) or (player1 == 2 and player2 == 1) \
        or (player1 == 3 and player2 == 2):
        return True

print(play())