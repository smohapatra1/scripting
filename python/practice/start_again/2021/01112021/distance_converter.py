# Convert the units

def convert(unit1, unit2, value):
    SI = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000}
    out = value * SI[unit1] /SI[unit2]
    print (str(value)  + unit1  + " " + "is" + " " + str(out ) + unit2 )

def main():
    unit1 = input("Enter the unit to convert from : ")
    unit2 = input("Enter the unit to convert to: ")
    value = float(input("Enter the value: " ))
    convert(unit1, unit2, value)

if __name__ == "__main__":
    main()