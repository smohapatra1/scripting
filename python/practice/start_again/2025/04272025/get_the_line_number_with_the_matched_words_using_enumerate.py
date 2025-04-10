#   https://www.geeksforgeeks.org/how-to-obtain-the-line-number-in-which-given-word-is-present-using-python/

def find_word(file_path, target_word):
    try:
        with open('file.txt', 'r') as file:
            for line_num, line in enumerate(file, start=1):
                if target_word in line:
                    return line_num
    except FileNotFoundError:
        print ("Error:  The file was not found")
    except Exception as e:
        print (f"An Error occurred: (e)")
    return None

file_path = 'file.txt'
word = 'am'
result = find_word(file_path, word)
if result:
    print (f"the word '{word}' was found in line number : {result}")
    print (f"the word '{word}' was not found in the file")
