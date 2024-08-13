#   https://www.geeksforgeeks.org/python-program-to-count-even-and-odd-numbers-in-a-list/

def CountEvenOdd(n):
    even_count = 0
    odd_count = 0  
    for i in range(len(n)):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print ("Number of even numbers are {} and Number of odd numbers are {}".format(even_count, odd_count))

if __name__ == "__main__":
    n = [ 1, 10, 12, 3, 5, 7 ]
    result = CountEvenOdd(n)
    