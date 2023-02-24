alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 


def caesar(plain_text, shift_amount):
    final_text = ""
    for word in plain_text:
        position = alphabet.index(word)
        if direction == "encode" :
            new_position = position + shift_amount
            final_text += alphabet[new_position]
        else:
            new_position = position - shift_amount

            final_text +=alphabet[new_position]
    print (f"New {direction} letter : {final_text}")

def caesar2(plain_text, shift_amount,cipher_direction):
    final_text = ""
    if cipher_direction == "decode" :
            shift_amount *= -1
    for word in plain_text:
        position = alphabet.index(word)
        new_position = position + shift_amount
        final_text += alphabet[new_position]
    print (f"New {direction} letter - Caesar2 : {final_text}")


def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

#if direction == "encode":
#  encrypt(plain_text=text, shift_amount=shift)
#elif direction == "decode":
#  decrypt(cipher_text=text, shift_amount=shift)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(plain_text=text, shift_amount=shift)
#A different Way 
caesar2(plain_text=text, shift_amount=shift, cipher_direction=direction)

