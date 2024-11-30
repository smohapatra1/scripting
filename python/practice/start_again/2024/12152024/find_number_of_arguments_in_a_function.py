#   https://www.geeksforgeeks.org/how-to-find-the-number-of-arguments-in-a-python-function/
def NumofArg(*args):
    return len(args)

if __name__ == "__main__":
    print("Total Args = ", NumofArg(2, 4, 6, 9 ))