#Convert Binary to decial number 
#https://www.geeksforgeeks.org/program-binary-decimal-conversion/

def calculate_dec(d):
    #One Way 
    #******************
    decimal = int(d,2)
    print ("First way  ", decimal)
    #Second Way
    #******************
    #first get position of the number 
    ar = [int(i) for i in d]
    ar = ar[::-1]
    res = []
    for i in range (len(ar)):
        res.append(ar[i]*(2**i))
    sum_res = sum(res)
    print ("Second Way", sum_res)
def main():
    d = input("Enter a binary number : ")
    calculate_dec(d)

if __name__ == "__main__":
    main()