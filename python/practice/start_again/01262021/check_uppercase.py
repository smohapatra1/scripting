#Check if a char is upper 

def main():
    a = str(input("Enter your name or some chars: "))
    if (a.isupper()):
        print ("{} is in UPPER".format(a))
    else:
        print ("{} is in NOT UPPER".format(a))

if __name__ == "__main__":
    main()