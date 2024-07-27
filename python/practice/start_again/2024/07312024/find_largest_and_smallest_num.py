#   How Do You Find the Largest and Smallest Number in an Array of 1–100?
import random

def LargestSmallest(num):
    large = -1
    small = 101
    for i in range(num):
        x = random.randint(1,100)
        small = min(x, small)
        large = max(x, large)
    print (small, large)

if __name__ == "__main__":
    num = 20
    result = LargestSmallest(num)