#   https://www.geeksforgeeks.org/python-program-match-string-random-strings-length/


import string
import random
import time


def Gen(x):
    possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'
    attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(x)))
    attemptNext = ''
    completed = False
    iteration = 0
    while completed == False: 
        print(attemptThis)  
        attemptNext = '' 
        completed = True
        
        # Fix the index if matches with  
        # the strings to be generated 
        for i in range(len(x)): 
            if attemptThis[i] != x[i]: 
                completed = False
                attemptNext += random.choice(possibleCharacters) 
            else: 
                attemptNext += x[i] 
                
        # increment the iteration  
        iteration += 1
        attemptThis = attemptNext 
        time.sleep(0.1) 
    print("Target matched after {}".format(iteration) + " iterations") 

if __name__ == "__main__":
    x = "geek"
    result = Gen(x)