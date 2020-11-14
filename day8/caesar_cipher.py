alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Don't change the code above 👆

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter not in alphabet:
            encrypted_text += letter
        else:
            pos = alphabet.index(letter)
            if pos + shift > 26:
                encrypted_text += alphabet[pos + shift -26]
            else:
                encrypted_text += alphabet[pos + shift]

    print(f"The encoded text is {encrypted_text}")

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        if letter not in alphabet:
            decrypted_text += letter
        else:
            pos = alphabet.index(letter)
            if pos - shift < 0:
                decrypted_text += alphabet[pos - shift + 26] 
            else:
                decrypted_text += alphabet[pos - shift]  
    print(f"The decoded text is {decrypted_text}")         

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)