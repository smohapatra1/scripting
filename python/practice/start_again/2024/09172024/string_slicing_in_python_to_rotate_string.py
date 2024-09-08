#   https://www.geeksforgeeks.org/string-slicing-python-rotate-string/

def rotate(input, d):
    lFirst = input[0:d]
    lSecond = input[d:]
    rFirst = input[0: len(input)-d]
    rSecond = input[len(input)-d]
    print ("Left Rotation - ", (lSecond + lFirst))
    print ("Right Rotation - ", (rSecond + rFirst))


if __name__ == "__main__":
    input = 'GeeksforGeeks'
    d=2
    rotate(input, d )