# Print a First non repeated chars in a string


def nonrepeat(s):
    ord = []
    count = {}
    for i in s:
        if i  in count:
            count [i] +=1
        else:
            count[i] = 1
            ord.append(i)
    for x in ord:
        if count[x] == 1:
            return x
    return None


if __name__ == "__main__":
    s = 'ababs'
    result = nonrepeat(s)
    print (result)