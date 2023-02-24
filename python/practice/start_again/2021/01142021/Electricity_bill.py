#Python Program to Calculate Electricity Bill
#Write a Python program to Calculate Electricity Bill with an example. For this, we are using Elif Statement.

def main():
    a = float(input("Enter your meter reading : "))
    if a > 100:
        unit = 2
        total_bill = a * unit 
        print ("Total Bill = ", total_bill)
    else:
        unit = 1 
        total_bill = a * unit 
        print ("Total Bill = ", total_bill)
if __name__ == "__main__":
    main()
