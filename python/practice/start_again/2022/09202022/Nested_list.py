# Given the names and grades for each student in a class of  students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and 
# print each name on a new line.
# Example 

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . 
# Ordered alphabetically, the names are printed as:
# alpha
# beta
# Input Format
# The first line contains an integer, , the number of students. 
# The  subsequent lines describe each student over  lines. 
# - The first line contains a student's name. 
# - The second line contains their grade.
# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format
# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, 
# order their names alphabetically and print each one on a new line.
# Sample Input 0
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0
# Berry
# Harry


if __name__ == '__main__':
    records = []
    scr= []
    for i in range(int(input("Enter the number of students: "))):
        name=input("Enter your name: ")
        score = float(input("Enter your score: "))
        records.append([name, score])
        scr.append(score)
    sot = list(set(scr))
    print (f"{sot}")
    sat= sorted(sot)
    print (f"{sat}")
    names=[]
    for n in records:
        if n[1] == sat[1]:
            names.append(n[0])
    for i in sorted(names):
        print (i)