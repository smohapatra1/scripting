# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.
# Sample Input 0
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika


# Sample Output 0
# 56.00

if __name__ == '__main__':
    student_marks = {}
    for i in range(int(input("Enter the number of students: "))):
        name, *line = input("Enter the student name and their marks: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter the student name: ")
    print (f"{sum(student_marks[query_name])/len(scores):.2f}")


