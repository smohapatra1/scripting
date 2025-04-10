#   https://www.geeksforgeeks.org/python-program-to-modify-the-content-of-a-binary-file/

def update(word, new):
    string = 'b'
    Flag = 0 
    with open ('file.txt', 'r+b') as file:
        pos = 0 
        data = string = file.read(1)
        while data:
            data = file.read(1)
            if data == "b":
                if string == word:
                    file.seek(pos)
                    file.write(new)
                    Flag = 1
                    break 
            else:
                string += data
                continue
    if Flag:
        print ("record successfuly uploaded")
    else:
        print ("Record not found")
word = input("Enter the word to be replaced")
new = input("\nEnter the new word: ").encode()
 
update(word, new)





