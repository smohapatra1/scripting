# #   https://leetcode.com/problems/maximum-frequency-stack/

# 895. Maximum Frequency Stack
# Hard
# 4.5K
# 66
# Companies
# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

# Implement the FreqStack class:

# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

# Example 1:

# Input
# ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
# [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
# Output
# [null, null, null, null, null, null, null, 5, 7, 5, 4]

# Explanation
# FreqStack freqStack = new FreqStack();
# freqStack.push(5); // The stack is [5]
# freqStack.push(7); // The stack is [5,7]
# freqStack.push(5); // The stack is [5,7,5]
# freqStack.push(7); // The stack is [5,7,5,7]
# freqStack.push(4); // The stack is [5,7,5,7,4]
# freqStack.push(5); // The stack is [5,7,5,7,4,5]
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
# freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
# freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
 
from collections import defaultdict
class FreqStack:

    def __init__ (self):
        self.set = defaultdict(list)
        self.freq=defaultdict(int)
        self.max_freq = 0 
    def push ( self, val: int) -> None:
        self.freq[val] +=1
        self.max_freq=max(self.max_freq, self.freq[val])
        self.set[self.freq[val]].append(val)

    def pop(self) -> int:
        val = self.set[self.max_freq].pop()
        self.freq[val] -=1
        if not self.set[self.max_freq]:
            self.max_freq -=1
        return val
