# #   https://www.hackerrank.com/challenges/favourite-sequence/problem?isFullScreen=true

# Johnny, like every mathematician, has his favorite sequence of distinct natural numbers. Let’s call this sequence . Johnny was very bored, so he wrote down  copies of the sequence  in his big notebook. One day, when Johnny was out, his little sister Mary erased some numbers(possibly zero) from every copy of  and then threw the notebook out onto the street. You just found it. Can you reconstruct the sequence?

# In the input there are  sequences of natural numbers representing the  copies of the sequence  after Mary’s prank. In each of them all numbers are distinct. Your task is to construct the shortest sequence  that might have been the original . If there are many such sequences, return the lexicographically smallest one. It is guaranteed that such a sequence exists.

# Note
# Sequence  is lexicographically less than sequence  if and only if there exists  such that for all .

# Input Format

# In the first line, there is one number  denoting the number of copies of .
# This is followed by 
# and in next line a sequence of length  representing one of sequences after Mary's prank. All numbers are separated by a single space.

# Constraints


# All values in one sequence are distinct numbers in range .

# Output Format

# In one line, write the space-separated sequence  - the shortest sequence that might have been the original . If there are many such sequences, return the lexicographically smallest one.

# Sample Input

# 2
# 2
# 1 3
# 3
# 2 3 4
# Sample Output

#  1 2 3 4
# Explanation

# You have 2 copies of the sequence with some missing numbers:  and . There are two candidates for the original sequence , where the first one is lexicographically least.


# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n = int(input())
before_maps = defaultdict(set)
after_maps = defaultdict(set)
for _ in range(n):
    k = int(input())
    sequence = map(int, input().split())
    prev = 0
    for num in sequence:
        if prev:
            before_maps[num].add(prev)
        after_maps[prev].add(num)
        prev = num

m = []
actives = set(active for active in after_maps[0] if not before_maps[active])
while actives:
    next_step = sorted(actives)[0]

    actives.remove(next_step)
    for step in after_maps[next_step]:
        before_maps[step].remove(next_step)

    actives.update(active for active in after_maps[next_step] if not before_maps[active])
    m.append(next_step)

print(' '.join(map(str, m)))