#   https://www.geeksforgeeks.org/problems/repeat-the-strings/1

def Repeat(a, b ):
    if len(a) > len(b):
        temp1 = a
        temp2 = b 
    else:
        temp1 = b 
        temp2 = a 
    return temp1 + temp2  + temp1
if __name__ == "__main__":
    a = 'Hi'
    b = 'Samar'
    print ("After repeating: ", Repeat(a, b ))