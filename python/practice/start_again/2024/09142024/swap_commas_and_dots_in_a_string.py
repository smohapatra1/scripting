#   https://www.geeksforgeeks.org/python-swap-commas-dots-string/


def Swap(str1):
    str1 = str1.replace(', ', 'third')
    str1 = str1.replace('.', ', ')
    str1 = str1.replace('third', '.')
    return str1

if __name__ == "__main__":
    string = "14, 625, 498.002"
    result = Swap(string)
    print (result)