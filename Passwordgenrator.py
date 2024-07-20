import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '*', '?', '^', '~']
print("Welcome to the password generator")
n_letters = int(input("How many letters will you want?\n"))
n_numbers = int(input("How many numbers will you want?\n"))
n_symbols = int(input("How many symbols will you want?\n"))
password = ""

for i in range(n_letters):
    password += random.choice(letters)

for i in range(n_numbers):
    password += random.choice(numbers)

for i in range(n_symbols):
    password += random.choice(symbols)
    
password = ''.join(random.sample(password, len(password)))

print("Your generated password is:", password)
