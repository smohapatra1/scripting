#   https://www.geeksforgeeks.org/python-program-for-removing-i-th-character-from-a-string/

def RemString(string, i ):
    a = string[:i]
    b = string[i+1:]
    return a+b 

if __name__ == "__main__":
    # string = "geeksFORgeeks"
    string = "Samar123456"
    # Remove nth index element 
    i = 5
    result = RemString(string, i)
    print (result)