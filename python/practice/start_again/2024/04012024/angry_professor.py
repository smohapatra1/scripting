# #   https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true

# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time () to arrived late ().

# Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

# Example




# The first  students arrived on. The last  were late. The threshold is  students, so class will go on. Return YES.

# Note: Non-positive arrival times () indicate the student arrived early or on time; positive arrival times () indicate the student arrived  minutes late.

# Function Description

# Complete the angryProfessor function in the editor below. It must return YES if class is cancelled, or NO otherwise.

# angryProfessor has the following parameter(s):

# int k: the threshold number of students
# int a[n]: the arrival times of the  students
# Returns

# string: either YES or NO
# Input Format

# The first line of input contains , the number of test cases.

# Each test case consists of two lines.

# The first line has two space-separated integers,  and , the number of students (size of ) and the cancellation threshold.
# The second line contains  space-separated integers () that describe the arrival times for each student.

# Constraints

# Sample Input

# 2
# 4 3
# -1 -3 4 2
# 4 2
# 0 -1 2 1
# Sample Output

# YES
# NO
# Explanation

# For the first test case, . The professor wants at least  students in attendance, but only  have arrived on time ( and ) so the class is cancelled.

# For the second test case, . The professor wants at least  students in attendance, and there are  who arrived on time ( and ). The class is not cancelled.


def AngryProfessor(k, a):
    count = 0 
    for i in a :
        if i <= 0:
            count +=1
    if k > count :
        return 'YES'
    else:
        return 'NO'



if __name__ == "__main__":
    t = int(input().strip())
    for t_iter in range(t):
        x = input().rstrip().split()
        n = int (x[0])
        k = int (x[1])
        a = list(map(int, input().strip().split()))
        result = AngryProfessor(k, a)
        print (result)