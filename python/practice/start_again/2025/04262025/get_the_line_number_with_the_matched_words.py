#   https://www.geeksforgeeks.org/how-to-obtain-the-line-number-in-which-given-word-is-present-using-python/

def find_word(file, target_word):
    line_num = 0
    with open(file, 'r') as file:
        for line in file:
            line_num +=1
            if target_word in line:
                return line_num
    return None
file = "file.txt"
word_to_find = "am"
line_num = find_word(file, word_to_find)
if line is not None:
    print (f"This word '{word_to_find}' is present in line number : {line_num}")
else:
    print (f"This word '{word_to_find}' is not found in the file")