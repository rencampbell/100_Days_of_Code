import random
from hangman_words import word_list
from hangman_art import stages, logo2, logo3

display=[]
lives=6

#function which selects and returns a random word from a list
def select_word (list):
    word=random.choice(list)
    return word

#function which determines if a given letter is part of a word
#returns true or false accordingly
def find_letter (word,letter):
    for w in word:
        if w==letter:
            match=True
            break
        else:
            match=False
    return match

#function which intitiates display to a list, the same size as the inputted word
#the list will be filled with '_'
def initiate_display (word):
    length=len(word)
    for position in range(length):
        display.append('_')
    return(display)

#function which updates display by replacing '_' if the letter is guessed correctly
def update_display (guess,word):
    length=len(word)
    for position in range(length):
        letter=word[position]
        if letter==guess:
            display[position]=letter
    return(display)

#prints logo from hangmant art module welcoming user to the game
print(logo3)

#runs the select_word function on list from the hangman_words module
#chooses a random word from the list
chosen_word=select_word(word_list)
# print(chosen_word)

#initiates_display eg ['_'.'_','_']
initial_display=initiate_display(chosen_word)
print(initial_display)

#initiates end_of_game as false
#this will change if lives=0 or the user guesses all letters
end_of_game=False

#while end_of_game is still false
while not end_of_game:

    #allows user to guess letter
    user_guess=input("Guess a letter: ").lower()

    #determines if guess is part of the word
    #returns true or false
    is_letter=find_letter(chosen_word,user_guess)
    #if guess is not part of the word
    if is_letter==False:
        print("This is not in the word.")
        #reduces lives
        lives-=1
        #ends game if lives=0
        if lives==0:
            end_of_game=True
            print("You lose!")

    #updates display based on if the letter is guessed correctly eg. ['_'.'a','_']
    new_display=update_display(user_guess,chosen_word)
    print(new_display)

    print(stages[lives])

    #ends game if all letters have been guessed correctly
    if "_" not in new_display:
        end_of_game=True
        print("You win!")
        print(logo2)




