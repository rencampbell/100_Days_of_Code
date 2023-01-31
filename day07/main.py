import random

word_list=["ardvark","baboon","camel"]

display=[]

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

    new_display=update_display(user_guess,chosen_word)
    print(new_display)

    if "_" not in new_display:
        end_of_game=True
        print("You win!")




