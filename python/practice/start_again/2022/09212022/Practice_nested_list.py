# Given the names and grades for each student in a class of  students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and 
# print each name on a new line.



if __name__ == '__main__':
    records=[]
    students=[]
    names=[]
    scores=[]
    for i in range(int(input("Enter number of students: "))):
        name=input("Enter student name: ")
        score=float(input("Enter their marks: "))
        records.append([name, score])
        scores.append(score)
    sot=list(set(scores))
    sat=sorted(sot)
    for n in records:
        if n[1] == sat[1]:
            names.append(n[0])
    for i in sorted(names):
        print (i)

