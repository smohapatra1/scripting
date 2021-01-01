#Fibonancci Series 

def main():
    i = []
    a = 1
    b = 1
    for x in range(10):
        i.append(a)
        a,b = b, a+b
    print (i)
if __name__ == '__main__':
    main()