import random

listofwords = ["familiar", "machine", "waiting", "cushion", "damage", "natural", "wonder", "religion", "tongue", "homeless", "daughter", "railway", "married", "dinosaur", "material"]
word = random.choice(listofwords)
print("\nWelcome to Hangman!\nYou will have 6 tries to try to guess the correct word.\nIf you don't guess the word correctly, you lose the game.")
max = 6
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letterguessed = []

while max >= 2:
    guess = input(" Guess a letter: ")
    if guess not in alpha:
        print("That's not a letter, try again.")
    elif guess not in word:
        max -= 1
        if max == 1: 
            print("Sorry, that letter is not in the word. Try again. 1 guess left.")
        else:
            print("Sorry, that letter is not in the word. Try again. " + str(max)+ " guesses left.")
    else:
        guess in word
        print("Good job! That letter is in the word.")

    for letter in word:
        letterguessed.append(guess)
        if letter in letterguessed: 
            print(letter, end="")
        else:
            print("_", end="")

while max == 1:
        yes_guess = input("\nYou have 1 guess left. Try to guess the word. ")
        if yes_guess == word:
            print ("\nCongragulations, you guessed the word correctly. You won the game!")
            break
        elif yes_guess != word:
            print("\nSorry, you didn't guess the word correctly. You lost the game.\nThe real word was " + str(word) + "!")
            break

print("-------------------------------------------------------------------")
#Last print statment inspired by Onyou Park