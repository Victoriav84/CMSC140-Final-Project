#Incomplete code. Random code everywhere, sorry if it doesn't make sense to you.
import random
#Test word. I want to use listofwords but don't know how to assign a number to each word for python to choose from.
word = "religion" 
#listofwords = ["familiar", "machine", "secretive", "waiting", "cushion", "hilarious", "invention", "damage", "natural", "scrawny", "wonder", "religion", "calculator", "tongue", "homeless", "daughter", "railway", "married", "dinosaur", "material"]

### Here's a method I often use for randomly choosing strings:
### This generates a random number and grabs that corresponding word from the dictionary
listofwords = {
    1 : "religion",
    2 : "familiar",
    3 : "machine",
    4 : "secretive",
    5 : "waiting", ### And so on
}
wordlistchoice = random.randint(1,5)
word = listofwords[wordlistchoice]

print("Welcome to Hangman!\nYou will have 6 tries to try to guess the correct word.\nIf you don't guess the word correctly, you lose the game.")
max = 6
### I recommend using the ord() function instead
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letterguessed = ""

#Having problems with this loop. 
while max > 0:
    guess = input("Guess a letter: ")
    if guess not in word:
        print("Sorry, that letter is not in the word. Try again. " + str(max)+ " guesses left.")
        max -= 1 ### Moved "max" guess counter to only reduce on wrong guesses
    if guess in word:
        print("Good job! That letter is in the word. "+ str(max)+ " guesses left.")
#    if guess not in word:
#        print("Sorry, that letter is not in the word.")     
    else :
        guess not in alpha
        print("That's not a letter, try again.")

#I don't know how to get correct letter in the dashes. Ex: if "i" is guessed, I want to print ___i_i__, but how would that work if python is choosing a word at random and almost all words have a different character count? 

### This is more difficult, but this website seems to have some good solutions: https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
### I would try checking making a list with each letter, then checking each letter against "letterguessed", then adding that letter to something like this:
### correctguesses = ["_", "_", "_", "_", "_"], then amending the list by replacing the corresponding underscore with the correct letter. 
### If, for example, the fifth letter of the word is "a", then check all letters in the word's letter list, then replace the underscore with the correct letter, then join and print the list.

    for letter in word:
        if letter in letterguessed:
            print(letter, end="")
        else:
            print("_", end="")
