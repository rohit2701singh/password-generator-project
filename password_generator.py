import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

num_in_password = [random.choice(numbers) for _ in range(nr_numbers)]
letters_in_password = [random.choice(letters) for _ in range(nr_letters)]
symbols_in_password = [random.choice(symbols) for _ in range(nr_symbols)]

password_list = num_in_password + letters_in_password + symbols_in_password
print(password_list)

easy_password = ""
for simple_password in password_list:
    easy_password += simple_password
print(f"your non-randomise easy password is: {easy_password}\n")


random.shuffle(password_list)
final_password = ''.join(password_list)
print(f"your randomise hard password is: {final_password}")








