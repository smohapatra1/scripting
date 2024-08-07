#   Counting the occurrences of elements in the list

def countOccur(days):
    x = set(days)
    print ([[y, days.count(y)] for y in x ])

if __name__ == "__main__":
    days = ['S','M','M','M','F','S']
    result = countOccur(days)