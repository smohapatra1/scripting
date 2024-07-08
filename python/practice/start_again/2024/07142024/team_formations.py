# #   https://www.hackerrank.com/challenges/team-formation/problem?isFullScreen=true

# For an upcoming programming contest, Roy is forming some teams from the students of his university. A team can have any number of contestants.

# Roy knows the skill level of each contestant. To make the teams work as a unit, he forms the teams based on some rules. Each of the team members must have a unique skill level for the team. If a member's skill level is  where , there exists another team member whose skill level is . Note that a contestant can write buggy code and thus can have a negative skill level.

# The more contestants on the team, the more problems they can attempt at a time so Roy wants to form teams such that the smallest team is as large as possible.

# For example, there are  contestants with skill levels . There are many ways teams could be formed, e.g. [-1], [0],...,[3]. At the other end of the spectrum, we could form  and . We're looking for the largest smaller team size though. Two sets that meet the criteria are  and . The largest smaller team size possible is .

# Note: There is an edge case where  contestants have registered. As no teams are to be created, the largest team created will have  members.

# Input Format

# The first line contains an integer , the number of test cases.

# Each of the next  lines contains a string of space-separated integers,  followed by  integers , a list of the contestants' skill levels.

# Constraints




# Output Format

# For each test case, print the size of largest possible smallest team on a separate line.

# Sample Input

# 4  
# 7 4 5 2 3 -4 -3 -5  
# 1 -4  
# 4 3 2 3 1  
# 7 1 -2 -3 -4 2 0 -1  
# Sample Output

# 3
# 1
# 1
# 7
# Explanation

# For the first case, Roy can form two teams: one with contestants with skill levels {-4,-3,-5} and the other one with {4,5,2,3}. The first group containing 3 members is the smallest.

# In the second case, the only team is {-4}

# In the third case, the teams are {3} , {1,2,3}, the size of the smaller group being 1.

# In the last case, you can build one group containing all of the contestants. The size of the group equals the total number of contestants.

# Time limits

# Time limits for this challenge are given here

# Note

# If n = 0, print 0.


# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq


def pop_from(dict, key):
    val = heapq.heappop(dict[key])
    if len(dict[key]) == 0:
        del dict[key]
    return val


def push_into(dict, key, value):
    if key not in dict:
        dict[key] = []
        heapq.heapify(dict[key])
    heapq.heappush(dict[key], value)


t = int(input())
for _ in range(t):
    A = list(map(int, input().split()))
    n = A[0]
    if n ==0:
        print(0)
    else:
        A = sorted(A[1:])
        teams = {}
        for i in range(n):
            if A[i] - 1 in teams:
                size = pop_from(teams, A[i] - 1)
                push_into(teams, A[i], size + 1)
            else:
                push_into(teams, A[i], 1)

        min_size = 999999
        for each in teams.values():
            min_pot = min(each)
            if min_pot < min_size:
                min_size = min_pot
        if min_size != 999999:
            print(min_size)