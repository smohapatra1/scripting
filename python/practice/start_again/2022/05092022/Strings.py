#Ask a user input. Check if the input include the letter 'a' or not. 
# If its true print as : "This input has a in it".
def string(text):
    if 'a' in text:
        print(f"This input {text} has 'a' in it")
    else:
        print (f"This input {text} has no 'a' in it ")


text=str(input("Enter a string: "))
string(text)