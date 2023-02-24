#Create password Generator 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print ("Welcome to the passwod Generator!\n")
letters_cnt=int(input("How many letters would you like in your password:\n"))
symbols_cnt=int(input("How many symbols would you like?\n"))
numbers_cnt=int(input("How many numbers would you like?\n"))

#Easy Levels - abqpAB12
password=""
for char in range (1,letters_cnt + 1):
    #get_letters=random.choice(letters)
    #password += get_letters
    #OR
    password +=random.choice(letters)
for symbol in range (1,symbols_cnt + 1):
    #get_symbols=random.choice(symbols)
    #password += get_symbols
    password +=random.choice(symbols)
for number in range (1,numbers_cnt + 1):
    #get_numbers=random.choice(numbers)
    #password += get_numbers
    password +=random.choice(numbers)
print (f"Password easy way: {password}")

#Hard levels - randomly
print ("Doing in a hard way...")
password_list = []
for char in range (1,letters_cnt + 1):
    password_list.append(random.choice(letters))
for symbol in range (1,symbols_cnt + 1):
    password_list.append(random.choice(symbols))
for number in range (1,numbers_cnt + 1):
    password_list.append(random.choice(numbers))
#print (password_list)
random.shuffle(password_list)
#print (password_list)
password=""
for char in password_list:
    password += char
print (f"Password hard way: {password}")
