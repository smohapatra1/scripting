# #   https://leetcode.com/problems/implement-stack-using-queues/

# 225. Implement Stack using Queues
# Easy
# 5.7K
# 1.2K
# Companies
# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
 

from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()   
    def push(x: int) -> None:
        tmp=deque[x]
        tmp.extend(self.deque)
        self.deque = tmp

    def pop() -> int:
        return queue.popleft()
        

    def top() -> int:
        return queue[0]
        

    def empty() -> bool:
        return len(queue) == 0
        
