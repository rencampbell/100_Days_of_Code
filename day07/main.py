import random
from hangman_words import word_list
from hangman_art import stages, logo2, logo3

display=[]
lives=6

def select_word (list):
    word=random.choice(list)
    return word

def find_letter (word,letter):
    for w in word:
        if w==letter:
            match=True
            break
        else:
            match=False
    return match

def initiate_display (word):
    length=len(word)
    for position in range(length):
        display.append('_')
    return(display)

def update_display (guess,word):
    length=len(word)
    for position in range(length):
        letter=word[position]
        if letter==guess:
            display[position]=letter
    return(display)



chosen_word=select_word(word_list)
print(chosen_word)

initial_display=initiate_display(chosen_word)
print(initial_display)

end_of_game=False

while not end_of_game:

    user_guess=input("Guess a letter: ").lower()

    is_letter=find_letter(chosen_word,user_guess)
    if is_letter==False:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose!")

    new_display=update_display(user_guess,chosen_word)
    print(new_display)

    print(stages[lives])

    if "_" not in new_display:
        end_of_game=True
        print("You win!")




