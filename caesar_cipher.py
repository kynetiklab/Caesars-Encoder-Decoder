#Caesar's Encoder
import string

def caesar_encode(message, offset):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            letters = string.ascii_letters
            if char.isupper():
                index = letters.index(char)
                encoded_char = letters[(index + offset) % 26]
            else:
                index = letters.index(char.lower())
                encoded_char = letters[(index + offset) % 26].lower()
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message

message = "We'll have dinner at your place tonight"
offset = 15
encoded_message = caesar_encode(message, offset)
print(encoded_message)


#Decoder

def caesar_decode(encoded_message, offset):
    decoded_message = ""
    letters = string.ascii_letters
    for char in encoded_message:
        if char.isalpha():
            if char.isupper():
                index = letters.index(char)
                decoded_char = letters[(index - offset + len(letters)) % len(letters)]
            else:
                index = letters.index(char.lower())
                decoded_char = letters[(index - offset + len(letters)) % len(letters)].lower()
            decoded_message += decoded_char
        else:
            decoded_message += char
    return decoded_message


encoded_message = "lt'aa wpkt sxcctg pi ndjg eaprt idcxvwi"
offset = 15
decoded_message = caesar_decode(encoded_message, offset)
print(decoded_message)
