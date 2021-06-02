#Boats to Save people
# In an arry find the people size and number of boats 

def boat_people(people):
    #people.sort()
    left = 0 
    right = len(people) -1
    boat_number=0
    limit = 3
    while left <= right:
        if left == right:
            boat_number +=1
            break
        if (people[left]+people[right]) <= limit:
            left +=1
        right -=1
        boat_number +=1
        #print (boat_number)
    return boat_number 
    
people = [2,1,3,4,5,6,2]
result = boat_people(people)
print (result)