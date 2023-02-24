#Boat to save people 
#Each people has some weight
# Certain boats carry certain weight
# Each boat carry 2 people with certain limit

#Solution 
#Sort the people
#Initialize the two pointers and initialize the boar numbers 


def save_boat(num_of_people):
    num_of_people.sort()
    left = 0 
    right = len(num_of_people) - 1 
    boat_numbers = 0 
    limit = 3 
    while left <= right :
        if left == right :
            boat_numbers += 1 
            break
        if (num_of_people[left]+num_of_people[right]) <= limit:
            left +=  1
            right -= 1
            boat_numbers += 1 
        else:
            right += 1
            boat_numbers += 1 
    return boat_numbers
            
num_of_people = [2,1,3,1]
save_boat(num_of_people)