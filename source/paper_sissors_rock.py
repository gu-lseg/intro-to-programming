import random

choices = ['paper', 'sissors', 'rock']
chosen = random.choice(choices)

while True:
    msg = 'Type one of following {}: '.format(' '.join(choices))
    usr = input(msg)
    if usr in choices:
        break
    print('Please choose a correct choice')

print('computer choses: {}'.format(chosen))

if usr == chosen:
    print('The result is a tie!')

if usr == 'paper':
    if chosen == 'rock':
        print('paper wins')
    else:
        print('rock wins')

if usr == 'sissors':
    if chosen == 'paper':
        print('sissors wins')
    else:
        print('rock wins')

if usr == 'rock':
    if chosen == 'sissors':
        print('rock wins')
    else:
        print('paper wins')
