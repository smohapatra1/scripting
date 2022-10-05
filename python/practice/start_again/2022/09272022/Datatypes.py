# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.

def data_rep(N):
    l=[]
    # for i in range(N):
    #     a=input().split()
    #     if a[0] == 'insert':
    #         l.insert(int(a[1]), int(a[2]))
    #     elif a[0] == 'remove':
    #         l.remove(a[1])
    #     elif a[0] == 'append':
    #         l.append(a[1])
    #     elif a[0] == 'sort':
    #         l.sort()
    #     elif a[0] == 'pop':
    #         l.pop()
    #     elif a[0] == 'reverse':
    #         l.reverse()
    #     else:
    #         print (l)
    for i in range(N):
        command_arg=input().strip().split()
        cmd=command_arg[0]
        args=command_arg[1:]
        if cmd == 'print':
            print (l)
        else:
            command="l.{0}{1}".format(cmd, ",".join(args))
            eval(command)


if __name__ == '__main__':
    N=int(input("Enter the number of arrays : "))
    data_rep(N)