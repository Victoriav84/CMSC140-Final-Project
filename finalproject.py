#Incomplete code. Random code everywhere, sorry if it doesn't make sense to you.
import random
#Test word. I want to use listofwords but don't know how to assign a number to each word for python to choose from.
word = "religion" 
#listofwords = ["familiar", "machine", "secretive", "waiting", "cushion", "hilarious", "invention", "damage", "natural", "scrawny", "wonder", "religion", "calculator", "tongue", "homeless", "daughter", "railway", "married", "dinosaur", "material"]

print("Welcome to Hangman!\nYou will have 6 tries to try to guess the correct word.\nIf you don't guess the word correctly, you lose the game.")
max = 6
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letterguessed = ""

#Having problems with this loop. 
while max > 0:
    guess = input("Guess a letter: ")
    max -= 1
    if guess not in word:
        print("Sorry, that letter is not in the word. Try again. " + str(max)+ " guesses left.")
    if guess in word:
        print("Good job! That letter is in the word. "+ str(max)+ " guesses left.")
#    if guess not in word:
#        print("Sorry, that letter is not in the word.")     
    else :
        guess not in alpha
        print("That's not a letter, try again.")

#I don't know how to get correct letter in the dashes. Ex: if "i" is guessed, I want to print ___i_i__, but how would that work if python is choosing a word at random and almost all words have a different character count? 
    for letter in word:
        if letter in letterguessed:
            print(letter, end="")
        else:
            print("_", end="")