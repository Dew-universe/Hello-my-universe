import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well', myName, ', I am thinking of a numbers between 1 and 20.')

for guessesTaken in range(6):
    print('Take a guess.') # Four spaces in front of 'print'
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.') #Eoght spaces in front of 'print'
    elif guess > number:
        print('Your guess is too high.')
    else:
        break

if guess == number:
    guessesTaken = guessesTaken + 1
    print('Good Job', myName, '! You quessed my number in ', guessesTaken, 'guessess!')
else:
    print('Nope. The number I was thinking of was', number, '.')

print('Press [ENTER] for exit.')
input()

