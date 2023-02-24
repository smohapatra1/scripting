#Python Program to find Student Grade
#Write a Python program to find Student Grade with an example. 
# For this, first, we have to calculate Total, and Percentage of Five Subjects. Next, use Elif to find the grade

def main():
    english = float(input("Enter the mark for English : "))
    math = float(input("Enter the mark for math : "))
    science = float(input("Enter the mark for science : "))
    hist = float(input("Enter the mark for hist : "))
    bio = float(input("Enter the mark for bio : "))
    Total = 500
    Pass = 70
    Total_mark = english + math + science+ hist+ bio
    percentage = (Total_mark / Total) * 100
    print ("Percentage : %.2f " % percentage)
    if percentage > Pass :
        print ("You are pass : %.2f" % percentage)
    else:
        print ( "You are Fail : %.2f" % percentage)

if __name__ == "__main__":
    main()