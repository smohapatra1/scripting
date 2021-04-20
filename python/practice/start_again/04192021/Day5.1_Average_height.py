#Average Height
#Instructions
#You are going to write a program that calculates the average student height from a List of heights.

#e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

#The average height can be calculated by adding all the heights together and dividing by the total number of heights.

#e.g.

#180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

#There are a total of 7 heights in student_heights

#1146 ÷ 7 = 163.71428571428572

#Average height rounded to the nearest whole number = 164

#Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

#Example Input
#156 178 165 171 187

#In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

#Example Output
#171

height_of_students=input("Enter the height of students with , separated: ").split(",")
number_of_students=len(height_of_students)
print (f"Number of students: {number_of_students}")
total_height=0
for item in height_of_students:
    print (f"\n{item}\n")
    total_height=total_height + int(item)
print (f"Total height : {total_height}")
avg=total_height / number_of_students
print (f"Average : {avg} and Round : {round(avg)}")

#Using sum and length function 
total_sum = sum(height_of_students)
total_len = len(height_of_students)
avg=round(total_sum / total_len)
print (f"avg: {avg}")


