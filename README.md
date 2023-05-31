**Caesar Cipher Encoder and Decoder**
This repository contains the encoder and decoder functions for a Caesar cipher implementation. The Caesar cipher is a simple substitution cipher that shifts each letter in the message by a certain number of positions in the alphabet.

**Encoder Function**
The encoder function takes a message and an offset as input and returns the encoded message using the Caesar cipher algorithm. It iterates over each character in the message, shifting alphabetic characters by the specified offset. Non-alphabetic characters are left unchanged. The encoded message is constructed by replacing each character with its shifted counterpart.

**Decoder Function**
The decoder function takes an encoded message and an offset as input and returns the decoded message. It follows the reverse process of the encoder function by shifting the alphabetic characters back to their original positions. Non-alphabetic characters are left unchanged.
