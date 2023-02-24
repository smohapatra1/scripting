#Print prime numbers between 1 - 100
def prime(a):
    for num in range(2,a):
        if num > 1:
            for j in range ( 2, num):
                if num % j == 0:
                    break
            else:
                prime.append(num)
                print (len)
prime(100)

