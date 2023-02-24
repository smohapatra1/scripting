#Highest Score
#Instructions
#You are going to write a program that calculates the highest score from a List of scores.

#e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

#Important you are not allowed to use the max or min functions. The output words must match the example. i.e

#The highest score in the class is: x

#Example Input
#78 65 89 86 55 91 64 89
#In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

#Example Output
#The highest score in the class is: 91

students_score=input("Enter students score with space: ").split()
highest_score = 0 
for score in students_score:
    if int(score) > int(highest_score) :
        highest_score = score
print (f"The highest score in the class is FOR loop: {highest_score}")

#Using max 
for score in students_score:
    print (score)
print (f"The highest score in the class is MAX function : {max(students_score)}")

