#Multiplication Table

def main():
    a = int(input("Enter the tables: "))
    b = int(input("Enter the numbers (1-10): "))
    for i in range(1, a+1):
        for j in range (1, b+1):
            print ("{} * {} = {}".format(i,j,i * j))
        print ("============")

if __name__ == "__main__":
    main()