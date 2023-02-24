#Distance Between Two Cities - [ Only Km and Miles ]
#Calculates the distance between two cities and allows the user to specify a unit of distance. 
#This program may require finding coordinates for the cities like latitude and longitude.


def calculate(c1,c2,unit):

    if unit == "km":
        if c1 > c2:
            diff = c1 - c2
            print ("Distance : %.2f %s " % (diff, unit))
        else:
            diff = c2 - c1
            print ("Distance : %.2f %s " % (diff, unit))
    else:
        miles_per_km = 0.621
        if c1 > c2:
            diff1 = c1 - c2
            diff = diff1 * miles_per_km
            print ("Distance : %.2f %s " % (diff, unit))
        else:
            diff2 = c2 - c1
            diff = diff2 * miles_per_km
            print ("Distance : %.2f %s " % (diff, unit))


def main():
    c1 = float(input("Enter the distance1 : "))
    c2 = float(input("Enter the distance2 : "))
    unit = str(input("Enter the conversion unit ( must be m. km, cm ): "))
    calculate(c1,c2,unit)

if __name__ == "__main__": 
    main()