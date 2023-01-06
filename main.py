SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'
translation = ""
print('Caesar Cipher')

while True:
    offset = input("Please enter an offset from 0 - 26 to encrypt: ")
    if int(offset.isdigit()) and int(offset) <= 26:
        break
    else:
        print("Please enter a valid offset.")

codeString = input("Please enter a string to encrypt: ")
lowerString = codeString.lower()

for char in lowerString:
    if char in SYMBOLS:
        num = SYMBOLS.find(char)
        num -= int(offset)
        translation = translation + SYMBOLS[num]
    else:
        translation = translation + char
print(translation)