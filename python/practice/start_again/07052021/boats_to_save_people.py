#Boats to Save people
#Boat can carry 2 people max
#Boat has a lmit of weight 
#Not each person can be carried more than once 

def save_people(people):
    #people.sort()
    left = 0 
    right = len(people) - 1 
    num_of_boats=0
    limit = 3 
    while left <= right:
        if left == right:
            num_of_boats+=1
            break
        if (people[left]+people[right]) <=limit:
            left +=1
        right -=1
        num_of_boats +=1
    return num_of_boats
people=[1,2,3,4,5]
result = save_people(people)
print (result)