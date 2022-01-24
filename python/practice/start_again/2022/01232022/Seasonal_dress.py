# Define a function that decides what to wear, according to the month and number of the day.
# It should ask for month and day number
# Seasons and Garments : 
# Sprint - Shirt
# Summer : T-Shirt 
# Autumn : Sweater 
# Winter : Coat 

def what_to_wear (m, d ):
    if m == "March"  and d < 15 or d > 20: 
        print (f'In {m}, day {d} Wear - Shirt ')
    elif m == "June" and d < 15 : 
        print (f'In {m}, day {d} wear : Shirt')
    elif m == "Decemember" and d < 15 :
        print (f'In {m}, day {d}  wear - Coat')

what_to_wear (str(input("Enter Month: ")), int(input("Enter day: ")))