#Head leg

def solve(number_legs, number_heads):
    for number_chickens in range(0, number_heads + 1):
        number_dogs = number_heads - number_chickens 
        total_legs = 4 * number_dogs + 2* number_chickens 
        if total_legs == number_legs: 
           return [number_dogs, number_chickens] 
    return[None, None] 

def animals():
    heads = int(input('Enter number of heads:')) 
    legs = int(input('Enter number of legs:'))
    dogs, chickens=solve(legs, heads)
    print (dogs)
    if dogs == None:
       print('there is no solution')
    else:
        print(f'number of dogs: {dogs}')
        print(f'number of chickes: {chickens}')
animals()
