import random

choices = ['paper', 'scissors', 'rock']
computer_choice = random.choice(choices)

while True:
    msg = 'Type one of following {}: '.format(' '.join(choices))
    user_choice = input(msg)
    if user_choice in choices:
        break
    print('Please choose a correct choice')

print('computer chooses: {}'.format(computer_choice))

if user_choice == computer_choice:
    print('The result is a tie!')
else:
    if user_choice == 'paper':
        if computer_choice == 'rock':
            print('paper wins')
        else:
            print('rock wins')

    if user_choice == 'scissors':
        if computer_choice == 'paper':
            print('scissors wins')
        else:
            print('rock wins')

    if user_choice == 'rock':
        if computer_choice == 'scissors':
            print('rock wins')
        else:
            print('paper wins')
