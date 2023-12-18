import random

print("\033[1m----- Welcome to the PyPassword Generator!\033[0m")
letters = int(input("How many \033[1mletters\033[0m would you like in your password?\n"))
symbols = int(input("How many \033[1msymbols\033[0m would you like?\n"))
numbers = int(input("How many \033[1mnumbers\033[0m would you like?\n"))

list_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
list_symbols = ["!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "_", "+"]

password = ""

for letter in range(1, letters + 1):
    password += list_letters[random.randint(0, len(list_letters) - 1)]

for symbol in range(1, symbols + 1):
    password += list_symbols[random.randint(0, len(list_symbols) - 1)]

for number in range(1, numbers + 1):
    password += str(random.randint(0, 9))

password = list(password)
random.shuffle(password)

print("Here is your new password: ", end="")
for char in password:
    print(f"{char}", end="")