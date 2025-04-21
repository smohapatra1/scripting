#   https://www.geeksforgeeks.org/python-finding-n-character-words-in-a-text-file/

def generate_n_char_words(file_path, n ):
    with open(file_path, 'r') as f:
        for line in f:
            for word in line.split():
                if len(word) == n:
                    yield word
file = 'file.txt'
n = 2
result = generate_n_char_words(file, n )
print (f"Words in {n} chars: ")
for word in result:
    print (word)
