import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
      ===  ''','''
  +---+
  O   |
      |
      |
      ===  ''','''
  +---+
  O   |
  |   |
      |
      ===  ''','''
  +---+
  O   |
/ |   |
      |
      ===  ''','''
  +---+
  O   |
/ | \ |
      |
      ===  ''','''
  +---+
  O   |
/ | \ |
 /    |
      ===  ''','''
  +---+
  O   |
/ | \ |
 / \  |
      ===  ''']
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar 
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion 
lizard llama mole monkey moose mule newt otter owl panda parrot pigeon python 
rabbit ram rat raven rhino salmon seal shark sheep shunk sloth snake spider 
stork swam tiger toad trout turkey turtle weasel whale wolf wombat zebra'''.split()

def getRandomWord(wordList):
    #This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0,len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replace blank with correctly guessed letter.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #Show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letters.')
        guess = input()
        guess = guess.lower()
        if len(guess) !=1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess
        
def playAgain():
    print('Do you want to play again?')
    return input().lower().startwith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won')
            gameIsDone = Done = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!',
                  'After',
                  str(len(missedLetters)),
                  'missed guesses and',
                  str(len(correctLetters)),
                  'correct guesses, the word was',
                  secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            gameIsDone = False
        else:
            break
