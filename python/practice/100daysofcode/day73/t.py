# Type your code here
def every(x):
    lists = []
    length = len(x)
    lists.append(x[0])
    for i in range(1, length):
        if i % 2 == 0:
            lists.append(x[i])
    print (lists)
every(["we", "love", "python", "so","much"])
