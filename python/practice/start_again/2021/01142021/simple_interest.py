#Python Program to Calculate Simple Interest
#Write a Python program to Calculate Simple Interest with example. 
#Before we get into the example, let me show you the formula behind the Simple Interest calculation:
#Simple Interest = (Principal Amount * Rate of Interest * Number of years) / 100

def SI(PA, ROI, NY):
    SI = (PA * ROI * NY)/100
    print ("Simple Interesti is %.2f" % SI)

def main():
    PA = float(input("Enter the principal Amount : "))
    ROI = float(input("Enter the ROI : "))
    NY = float(input("Enter the years: "))
    SI( PA, ROI, NY)

if __name__ == "__main__":
    main()