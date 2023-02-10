from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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

def cipher (text_c, shift_c, direction_c):    
    cipher_text=""
    if shift_c>25:
        shift_c=shift_c%26
    for char in text_c:
        if char in alphabet:
            position=alphabet.index(char)
            if direction_c=="e":
                new_position=position+shift_c
            else:
                new_position=position-shift_c
            new_letter=alphabet[new_position]
            cipher_text+=new_letter
        else: 
            cipher_text += char
    return cipher_text

print(logo)

direction=input("Type E to encrypt and D to decrypt: ").lower()
if direction!='e' and direction!='d':
    print("Please enter a valid input. ")
else:
    text=input("Please enter word: ").lower()
    shift=int(input ("Please enter shift amount: "))


new_text=cipher(text,shift,direction)
print(f"Your encrypted message is: {new_text}")


