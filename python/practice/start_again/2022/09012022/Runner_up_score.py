#Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. 
# You are given scores. Store them in a list and find the score of the runner-up.
import os
import sys
import math

if __name__ == '__main__':
    n=int(input("Number of runners: "))
    a=map(int, input().split())
    a = list(set(a))
    a.remove(max(a))
    print (max(a))
