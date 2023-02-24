#Weight to mass convertion 

def main():
    m = float(input("Enter your weight in lb : "))
    kg = float(m /2.2)
    print ("%.2f lb in kg : %.2f" % (m, round(kg,2)))
    k = float(input("Enter youe weight in KG: "))
    lb = float( k * 2.2)
    print ("%.2f kg in lb : %.2f" % (k, round(lb,2)))

if __name__ == "__main__":
    main()