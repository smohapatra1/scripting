#   https://www.geeksforgeeks.org/built-in-modules-in-python/

import random
num = random.randint(1, 10)
print (f"Random integers 1 to 10 : {num}")
fruits = ["Java", "C", "c+"]
choose_fruit = random.choice(fruits)
print(f"Randomly chosen language: {choose_fruit}")