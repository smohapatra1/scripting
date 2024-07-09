# #   https://www.hackerrank.com/challenges/fighting-pits/problem?isFullScreen=true

# Meereen is famous for its fighting pits where fighters fight each other to the death.

# Initially, there are  fighters and each fighter has a strength value. The  fighters are divided into  teams, and each fighter belongs exactly one team. For each fight, the Great Masters of Meereen choose two teams,  and , that must fight each other to the death. The teams attack each other in alternating turns, with team  always launching the first attack. The fight ends when all the fighters on one of the teams are dead.

# Assume each team always attacks optimally. Each attack is performed as follows:

# The attacking team chooses a fighter from their team with strength .
# The chosen fighter chooses at most  fighters from other team and kills all of them.
# The Great Masters don't want to see their favorite fighters fall in battle, so they want to build their teams carefully and know who will win different team matchups. They want you to perform two type of queries:

# 1 p x Add a new fighter with strength  to team . It is guaranteed that this new fighter's strength value will not be less than any current member of team .
# 2 x y Print the name of the team that would win a matchup between teams  and  in their current state (recall that team  always starts first). It is guaranteed that .
# Given the initial configuration of the teams and  queries, perform each query so the Great Masters can plan the next fight.

# Note: You are determining the team that would be the winner if the two teams fought. No fighters are actually dying in these matchups so, once added to a team, a fighter is available for all future potential matchups.

# Input Format

# The first line contains three space-separated integers describing the respective values of  (the number of fighters),  (the number of teams), and  (the number of queries).
# Each line  of the  subsequent lines contains two space-separated integers describing the respective values of fighter 's strength, , and team number, .
# Each of the  subsequent lines contains a space-separated query in one of the two formats defined in the Problem Statement above (i.e., 1 p x or 2 x y).

# Constraints

# It is guaranteed that both teams in a query matchup will always have at least one fighter.
# Scoring
# This challange has binary scoring. This means you will get a full score if your solution passes all test cases; otherwise, you will get  points.

# Output Format

# After each type  query, print the name of the winning team on a new line. For example, if  and  are matched up and  wins, you would print .

# Sample Input

# 7 2 6
# 1 1
# 2 1
# 1 1
# 1 2
# 1 2
# 1 2
# 2 2
# 2 1 2
# 2 2 1
# 1 2 1
# 1 2 1
# 2 1 2
# 2 2 1
# Sample Output

# 1
# 2
# 1
# 1
# Explanation

# Team  has three fighters with the following strength levels: .
# Team  has four fighters with the following strength levels: .

# The first query matching up team  and  would play out as follows:

# Team  attacks  The fighter with strength  can kill one fighter with strength  and one fighter with strength . Now, , and .
# Team  attacks  The fighter with strength  can kill the fighter with strength . Now, , and .
# Team  attacks  The fighter with strength  can kill one fighter with strength . Now, , and .
# Team  attacks  The fighter with strength  can kill one fighter with strength . Now, , and .
# Team  attacks  The fighter with strength  can kill the last fighter with strength . Now, , and .
# After this last attack, all of Team 's fighters would be dead. Thus, we print  as team  would win that fight.

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'fightingPits' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY fighters
#  3. 2D_INTEGER_ARRAY queries
#

def readints():
    return [int(x) for x in input().strip().split()]


class Team():
    def __init__(self, id, strengths):
        self.id = id
        self.strengths = sorted(strengths)
        self._beatable_sizes = defaultdict(lambda: [self.strengths[0]])
        self._least_winning_index = defaultdict(int)
        self.N = len(self.strengths)
        self.sum = sum(self.strengths)

    def __len__(self):
        return len(self.strengths)

    def __getitem__(self, idx):
        return self.strengths[idx]

    def add(self, strength):
        assert not self.strengths or strength >= self.strengths[-1]
        self.N += 1
        self.sum += strength
        self.strengths.append(strength)

    def simulate_fight(self, opponent, memoize=False):
        return self.id if self.can_beat(opponent, memoize) else opponent.id

    def can_beat(self, opponent, memoize):
        if memoize:
            return self.beatable_size(opponent) >= opponent.N
        else:
            i_self = self.N - 1
            i_opponent = opponent.N - 1
            while i_self >= 0:
                i_opponent -= self[i_self]
                if i_opponent < 0:
                    return True
                i_self -= opponent[i_opponent]
            return False

    def beatable_size(self, opponent):
        bs = self._beatable_sizes[opponent]
        lwi = self._least_winning_index
        for i in range(len(bs), self.N):
            for lwi[opponent] in range(lwi[opponent], opponent.N):
                idx = i - opponent[lwi[opponent]]
                if idx < 0 or lwi[opponent] >= bs[idx]:
                    break
            else:
                return opponent.N
            bs.append(lwi[opponent] + self[i])
        return bs[-1]


def main():
    team = {}

    N, K, Q = readints()
    for n in range(N):
        s, t = readints()
        team.setdefault(t, []).append(s)

    for k, v in team.items():
        t = Team(k, team[k])
        team[k] = t

    
    num_matches = defaultdict(int)
    queries = []
    for q in range(Q):
        qt, *args = readints()
        if qt == 2:
            key = frozenset(args)
            num_matches[key] += 1
            args += [key] 
        queries.append((qt, args))

    memoize_set = set(k for k, v in num_matches.items() if v >= 1000)
    for qt, args in queries:
        if qt == 1:
            p, x = args
            team.setdefault(x, Team(x, [])).add(p)
        else:
            x, y, key = args
            print(team[x].simulate_fight(team[y], key in memoize_set))


if __name__ == '__main__':
    main()
    

# def fightingPits(k, fighters, queries):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     q = int(first_multiple_input[2])

#     fighters = []

#     for _ in range(n):
#         fighters.append(list(map(int, input().rstrip().split())))

#     queries = []

#     for _ in range(q):
#         queries.append(list(map(int, input().rstrip().split())))

#     result = fightingPits(k, fighters, queries)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
