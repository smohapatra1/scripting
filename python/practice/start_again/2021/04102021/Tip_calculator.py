#Enter your bill
#provide the tips
#Split the bill
bill=float(input("Enter your bill amount: "))
tips=float(input("Enter the tips amount : "))
tips_percentage=float(tips/100)
friends=float(input("Enter the number of friends : "))
tips_total=(bill + tips_percentage)
total=((bill + tips ))
pays=round(float(total / friends), 2)
print(f"Each person should pay ${pays} Total Bill - ${total} and tips {tips} %")

