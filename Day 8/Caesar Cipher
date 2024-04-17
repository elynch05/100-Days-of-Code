from art import logo
import math
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
def caesar(direction, text, shift):
    new_text=text
    shift_amount=shift
    cipher_text = ""
    if direction == "encode":
        for letter in new_text:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")
        
    elif direction == "decode":
        for letter in new_text:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            cipher_text += alphabet[new_position]
        print(f"The decoded text is {cipher_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction=direction, text=text, shift=shift)     
    
    while True:
        more = input("Would you like to do another word? Y/N?: ").lower()
        if more == "y":
            break
        elif more == "n":
            print("Goodbye :)")
            exit()

