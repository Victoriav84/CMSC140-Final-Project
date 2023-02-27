#Incomplete code. Random code everywhere, sorry if it doesn't make sense to you.
import random
#Test word. I want to use listofwords but don't know how to assign a number to each word for python to choose from.
# Each list / array in python contain an index, so you could try doing: "for index in list:" this will traverse the list based on index
word = "religion" 
#listofwords = ["familiar", "machine", "secretive", "waiting", "cushion", "hilarious", "invention", "damage", "natural", "scrawny", "wonder", "religion", "calculator", "tongue", "homeless", "daughter", "railway", "married", "dinosaur", "material"]

print("Welcome to Hangman!\nYou will have 6 tries to try to guess the correct word.\nIf you don't guess the word correctly, you lose the game.")
max = 6
# alpha[0] will return the letter 'a', since the first item in any list starts with 0, so index = 1 is the position of letter 'b'
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letterguessed = ""

#Having problems with this loop.
while max > 0:
    guess = input("Guess a letter: ")
    max -= 1
    if guess not in word:
        print("Sorry, that letter is not in the word. Try again. " + str(max)+ " guesses left.")
    # structure tends to be first if, then elif, then else. elif means else if.
    if guess in word:
        print("Good job! That letter is in the word. "+ str(max)+ " guesses left.")
#    if guess not in word:
#        print("Sorry, that letter is not in the word.")     
    else :
        guess not in alpha
        print("That's not a letter, try again.")

#I don't know how to get correct letter in the dashes. Ex: if "i" is guessed, I want to print ___i_i__, but how would that work if python is choosing a word at random and almost all words have a different character count? 
 # you can make it so you get the index position of the letter they guessed, then only print the already guessed letters in their respective positions, and print udnerscores for the rest. 
 # This requires for you to keep track of the word length, letter positions relative to the entire word, and which words have already been guessed.
    for letter in word:
        if letter in letterguessed:
            print(letter, end="")
        else:
            print("_", end="")