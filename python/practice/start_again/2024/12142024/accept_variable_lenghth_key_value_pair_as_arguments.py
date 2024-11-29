#   https://www.geeksforgeeks.org/functions-that-accept-variable-length-key-value-pair-as-arguments/

def printKargs(**kwargs):
    print (kwargs)

if __name__ == "__main__":
    printKargs(Arg1='gfg', Arg2='GFG')