#Python Program to Calculate Profit or Loss
#Write a Python Program to Calculate Profit or Loss with a practical example.

def main():
    sale = int(input("Enter the sale price: "))
    buy = int(input("Enter the purchase amount: "))
    if sale > buy:
        print ("Net profit: ", sale - buy )
    elif sale < buy:
        print ("Net loss: ", sale - buy )
    else:
        print ("NO loss and NO profit")
if __name__ == "__main__":
    main()