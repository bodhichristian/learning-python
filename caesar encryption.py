
# Caesar's Encrytion
# Returns an encrpyted message where each letter is shifted by a specified `offset`.
def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

text = 'Hello Zaira'
shift = 3

caesar(text, shift)


