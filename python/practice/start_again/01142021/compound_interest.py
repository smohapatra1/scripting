#Python Program to Calculate Compound Interest
#Write a Python program to Calculate Compound Interest with example. 
#Before we start the Python compound Interest program, let me show you the formula behind this Compound Interest:

    #Future Compound Interest = Principal Amount * ( 1 + Rate of Interest ) ** Number of years)
    #The above calculation called Future Compound Interest. Because it contains both Principal Amount & Compound Interest. To get Compound Interest, use the below formula:
    #Compound Interest = Future Compound Interest – Principal Amount

def CI(PA,ROI,NY):
    FCI = PA * ( 1 + ROI) ** NY
    print ("Future CI : %.2f" % FCI)
    CI =  FCI - PA
    print ("Count Intrest : %.2f " % CI)

def main():
    PA  = float(input("Enter the principal Amount : "))
    ROI = float(input("Enter the ROI : "))
    NY  = float(input("Enter the years: "))
    CI( PA, ROI, NY)

if __name__ == "__main__":
    main()