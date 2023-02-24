#Try, expect and Finally 
def integer():
    try:
        x = int(input("Enter an integer : "))
    except:
        print ("Expect and Integer ")
    finally:
        print ("It's an integer") 
if __name__ == "__main__":
    integer()