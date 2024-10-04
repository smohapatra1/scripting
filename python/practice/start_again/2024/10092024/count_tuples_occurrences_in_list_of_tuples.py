#   https://www.geeksforgeeks.org/python-count-tuples-occurrence-in-list-of-tuples/
import collections

def Count(Input):
    Output = collections.defaultdict(int)
    for ele in Input:
        Output[ele[0]] +=1
    return Output


if __name__ == "__main__":
    # Input = [('hi', 'bye'),('Geeks', 'forGeeks'),('a', 'b'),('hi', 'bye'),('a', 'b')]
    Input = [[('hi', 'bye')], [('Geeks', 'forGeeks')],[('a', 'b')], [('hi', 'bye')], [('a', 'b')]]
    result = Count(Input)
    print (result)