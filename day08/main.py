from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt (text_e, shift_e):
#     cipher_text=""
#     for letter in text_e:
#         position=alphabet.index(letter)
#         new_position=position+shift_e
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter
#     return cipher_text

# def decrypt (text_d, shift_d):
#     cipher_text=""
#     for letter in text_d:
#         position=alphabet.index(letter)
#         new_position=position-shift_d
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter
#     return cipher_text

#defines the caesar cipher function
#this shifts the text_c(string) by shift_c(int) places in direction_c(char) direction
#if direction_c=e then the message is encoded, otherwise it is decoded
def cipher (text_c, shift_c, direction_c):    
    cipher_text=""
    #prevents errors if shift_c is larger than the size of the alphabet array
    if shift_c>25:
        shift_c=shift_c%26
    #loops through the inputted phrase
    for char in text_c:
        #if the char in text_c is present in the alphabet array (this excludes spaces and special characters)
        if char in alphabet:
            position=alphabet.index(char)
            if direction_c=="e":
                new_position=position+shift_c
            else:
                new_position=position-shift_c
            new_letter=alphabet[new_position]
            cipher_text+= new_letter
        #if the char in  text_c is not a member of the alphabet
        else: 
            cipher_text += char
    return cipher_text

print(logo)

go_again=True

#while loop responsible for exiting or restarting the main program
while go_again==True:

    direction=input("Type E to encrypt and D to decrypt: ").lower()
    if direction!='e' and direction!='d':
        print("Please enter a valid input. ")
    else:
        text=input("Please enter phrase: ").lower()
        shift=int(input ("Please enter shift amount: "))

    new_text=cipher(text,shift,direction)
    print(f"Your encrypted message is: {new_text}")

    go=input("Type Y to go again and N to exit: ").upper()

    if go =='Y':
        go_again= True
        print("\n")
    else:
        go_again= False




