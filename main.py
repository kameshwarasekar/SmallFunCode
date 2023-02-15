# Welcome to a simple game of Rock-Paper-Scissor-Lizard-Spock
"""
The rules are simple:
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
(and as it always has) Rock crushes Scissors
"""

from random import randint

flag = True
playOptions = ['rock', 'paper', 'scissor', 'lizard', 'spock']
# Possible to do with bunch of if-else of switch case, but dictionary is quicker
winner_list = {'rock': ['scissor', 'lizard'],
               'paper': ['rock', 'spock'],
               'scissor': ['lizard', 'paper'],
               'lizard': ['spock', 'paper'],
               'spock': ['scissor', 'rock']
               }
while flag:
    computer = playOptions[randint(0, 4)]
    flag = False
    print('Can you beat the Computer, Enter your choice:')
    choice = playOptions[int(input(' 1.Rock\n 2.Paper\n 3.Scissor\n 4.Lizard\n 5.Spock\n Your choice is : ' ))-1]
    if choice == computer:
        print('Tie, both you and the computer chose {}'.format(choice))
    else:
        if choice in winner_list[computer]:
            print('You won. Great choice of {}, the computer lost choosing {}'.format(choice,computer))
        else:
            print('You lose, you chose {} but the computer got lucky choosing {}'.format(choice,computer))
    flag = input('press c if you wanna try again: ') == 'c'

