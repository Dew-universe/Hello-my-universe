import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you, 
you see three caves. In one cave, the dragon is friendly 
and will share his treasure with you. The other dragon 
is greedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2'and cave !='3':
        print('Which cave will you go into? (1 or 2 or 3)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jump out in front of you! HE opens his jaws and...')
    time.sleep(2)

    friendlyCave = random.randint(1,3)

    if chosenCave == str(friendlyCave):
        print('Give you his treasure! :)')
    else:
        print('Gobbles you down in one bite! :(')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    print('-'*60)
    displayIntro()
    caveNumber =chooseCave()
    checkCave(caveNumber)

    print()
    print('Do you want to play again? (yes or no)')
    playAgain = input()

