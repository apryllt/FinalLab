import sys

cipher_text = ""
char_counter = 0
line_counter = 0

rotation = int(sys.argv[1])

plain_text = sys.stdin.read()

for character in plain_text:
    if character.isalpha():
        character = character.upper()
        shifted_char = chr((ord(character) - 65 + rotation) % 26 + 65)
        cipher_text += shifted_char
        char_counter += 1
        line_counter += 1

        if char_counter == 5:
            cipher_text += " "
            char_counter = 0

        if line_counter == 50:
          cipher_text += "\n"
          line_counter = 0

print(cipher_text)