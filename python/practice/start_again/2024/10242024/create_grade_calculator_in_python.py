#   https://www.geeksforgeeks.org/program-create-grade-calculator-in-python/

def CalculateGrade(total1, total2, total3, total4, total5):
    tot = total1 + total2 + total3 + total4 + total5
    avg = tot/5
    print (avg)
    if avg >= 91 and avg <=100:
        return 'Your Garde is A1'
    elif avg >=81 and avg <=91:
        return 'Your Garde is A2'
    elif avg >= 71 and avg < 81:
        return 'Your Grade is B1'
    elif avg >= 61 and avg < 71:
        return 'Your Grade is B2'
    elif avg >= 51 and avg < 61:
        return 'Your Grade is C1'
    elif avg >= 41 and avg < 51:
        return 'Your Grade is C2'
    elif avg >= 33 and avg < 41:
        return 'Your Grade is D'
    elif avg >= 21 and avg < 33:
        return 'Your Grade is E1'
    elif avg >= 0 and avg < 21:
        return 'Your Grade is E2'
    else:
        print ("Invalid Input")

if __name__ == "__main__":
    print("Enter Marks Obtained in 5 Subjects: ")
    total1 = 44
    total2 = 67
    total3 = 76
    total4 = 99
    total5 = 99
    print ("Your Grade is : ", CalculateGrade(total1, total2, total3, total4, total5))