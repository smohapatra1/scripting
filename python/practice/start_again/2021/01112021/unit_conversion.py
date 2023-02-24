#Unit Cconversion - m, mm, cm, km etc..

types = {
    "km" : 100000,
    "m" : 100,
    "cm": 1,
    "": 1
}

def convert( unit1, unit2, value):
    from_units = types[unit1]
    to_units = types[unit2]
    new_value = value * ( from_units/ to_units)
    print (str(new_value) + unit2)

def main():

    conversions = { 
        "mm ": {"mm":1, "cm": 1/10, "m": 1/1000, "km": 1/1000000},
        "cm ": {"mm":10, "cm": 1, "m": 1/100, "km": 1/100000},
        "m ": {"mm": 100, "cm": 100, "m": 1, "km": 1/1000},
        "km ": {"mm": 100000, "cm": 10000, "m": 1000, "km": 1},
                  }
    unit1 = input("Enter the unit you are trying to convert from? We support: "+", ".join(conversions.keys())).lower() 
    unit2 = input("Enter the unit you want to convert to? We support: "+", ".join(conversions.keys())).lower() 
    value = float(input("Enter the value to convert : "))     
    convert (unit1, unit2, value)
            

if __name__ == "__main__":
    main()