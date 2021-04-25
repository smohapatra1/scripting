#Grading Program
#Instructions
#You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

#Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

#DO NOT modify lines 1-7 to change the existing student_scores dictionary.

#DO NOT write any print statements.

#This is the scoring criteria:

#Scores 91 - 100: Grade = "Outstanding"

#Scores 81 - 90: Grade = "Exceeds Expectations"

#Scores 71 - 80: Grade = "Acceptable"

#Scores 70 or lower: Grade = "Fail"

#Expected Output
#'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'

student_scores = {
    "sam" : 90,
    "jon" : 50,
    "tom" : 88,
    "harry" : 60,
    }
student_grades = {}    
for student in student_scores: 
    score = student_scores[student]
    #print (student)
    if score >= 90 :
        student_grades[student] = "Outstanding"
        print (f"{student} - {student_grades[student]} - {score} ")
    elif score > 70:
        student_grades[student] = "Exceeds Expectations"
        print (f"{student} - {student_grades[student]} - {score} ")
    else:
        student_grades[student] = "Fail"
        print (f"{student} - {student_grades[student]} - {score} ")