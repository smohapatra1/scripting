#   How do you get the matching elements in an integer array?


def MatchingElement(n1):
    n2 = []
    for i in range(len(n1)):
        for j in range(i+1, len(n1)):
            if (n1[i] == n1[j] and (n1[i] not in n2)):
                n2.append(n1[i])
    print (n2)

if __name__ == "__main__":
    n1 = list(map(int,input().split()))
    result = MatchingElement(n1)
    # print (result)