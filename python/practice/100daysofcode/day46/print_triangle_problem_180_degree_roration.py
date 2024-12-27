def triangle_180(n):
    #Number of spaces
    if n <= 50:
        k = 2*n - 2
        for i in range(0,n):
            for j in range(0,k):
                print (end =" ")
            # decrementing k after each loop
            k = k - 2
            for j in range(0, i+1):
                print ("* ", end="")
            print ("\r")
    else:
        print ("Out of range")
triangle_180(int(input("Enter number : ")))
