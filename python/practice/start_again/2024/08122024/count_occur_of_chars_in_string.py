# Python Program to count occurrence of characters in string

def countOccur(n):
    count1 = 0 
    count2 = 0 
    for i in range(len(n)):
        if n[i] == ch1:
            count1 += 1
        elif n[i] == ch2:
            count2 += 1
    print ("{} count is {} and {} count is {}".format(ch1, count1, ch2, count2 ))


if __name__ == "__main__":
    n = 'python'
    ch1 = 'p'
    ch2 = 'e'
    result = countOccur(n)