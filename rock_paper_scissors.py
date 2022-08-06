import random

def play():
    while True:
        user = input("What's your choice? 'rock' for rock, 'paper' for paper, 'scissors' for scissors \n")
        computer =random.choice(['rock', 'paper', 'scissors'])

        print(f'You chose: {user}')
        print(f'Computer chose: {computer}')

        if user == computer:
            return 'It\'s a tie'

        # r>s, s>p, p>r
        if is_win(user, computer):
            return 'You won!'

        else: print('You lost!')

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break



def is_win(player, opponent):
    #return true if player wins
    #r > s, s > p, p > r
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') \
        or (player == 'paper' and opponent == 'rock'):
        return True

print(play())