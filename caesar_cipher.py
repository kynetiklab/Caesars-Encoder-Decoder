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


#Decoder without knowing the offset

def caesar_decode_no_ascii(coded_message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_messages = []
    
    # Loop through all possible shifts 1 to 26
    for i in range(1, 26):
        # An empty string to store the decoded message for the current shift
        decoded_message = ""
        
        # Loop through each character in the coded message
        for char in coded_message:
            # If the character is not a letter, add it to the decoded message as it is
            if not char.isalpha():
                decoded_message += char
            else:
                # Calculate the new index of the character after shifting
                new_char_idx = (alphabet.index(char.lower()) - i) % 26
                # Find the corresponding new character based on the new index
                new_char = alphabet[new_char_idx]
                # Add the new character to the decoded message with the same case as the original character
                decoded_message += new_char.upper() if char.isupper() else new_char
        
        # Add the decoded message for the current shift to the list of decoded messages
        decoded_messages.append(decoded_message)
    
    # Return the list of all decoded messages
    return decoded_messages

# Call the function with coded message as the argument
decoded_messages = caesar_decode_no_ascii("lt'aa wpkt sxcctg pi ndjg eaprt idcxvwi")
print(decoded_messages)
