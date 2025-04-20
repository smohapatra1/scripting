#   https://www.geeksforgeeks.org/python-finding-n-character-words-in-a-text-file/

def find_words_with_three_chars(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        words = content.split()
        words_with_three_chars = [word for word in words if len(word) == 3]
        return words_with_three_chars
file = 'file.txt'
result = find_words_with_three_chars(file)
print ("Words in 3 chars {}".format(result))