#Find which day of week

def day_of_week(n):
    # print (f"{type(n)}")
    # if type(n) != "int" :
    #     print ("Please enter an integer")     
    # else:
    #     n=int(n)
        if n < 1 or n > 7:
            print ("Please enter the number between 1 and 7")
        else:

            if n == 1 :
                print (f"Monday")
            elif n == 2 :
                print (f"Tuesday")
            elif n== 3 :
                print (f"Wednesday")
            elif n== 4:
                print (f"Thursday")
            elif n== 5:
                print (f"Friday")
            elif n== 6:
                print (f"Saturday")
            else:
                print (f"Sunday")
day_of_week(int(input("Enter the number: ")))