# From text 'Monday Tuesday Wednesday Thursday Friday'
# Find the first 3 characters
# Find the chars between index 7 and 10
# Find the chars between index 2 and 12 
# Find the chars at indicies 3, 4 and 5

#Case-1
text='Monday Tuesday Wednesday Thursday Friday'
def slice(text):
    #for letter in text:
        # First 3 letters 
        print (f" First 3 chars - {text[:3]}")
        # Chars between 7 and 10
        print (f" Chars between 7 and 10 - {text[7:11]}")
        # Chars between 2 and 12
        print (f" Chars between 2 and 12 - {text[2:12]}")
        # Chars between 3,4 and 5
        print (f" Chars between 3, 4 and 5 - {text[3:6]}")
slice(text)