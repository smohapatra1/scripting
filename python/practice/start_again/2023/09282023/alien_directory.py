# #   https://algo.monster/liteproblems/269
# Problem Explanation

# The problem refers to a new language that we have to infer from a list of words given to us. These words are sorted into the new language's lexicographical order, and the objective is to discern the order of the letters in the language.

# We are given some key requests to consider:

# The words comprise lowercase Latin alphabet letters.
# If word 'a' is a prefix of another word 'b', then 'a' should show up before 'b' in the provided list.
# If the order is invalid, we return an empty string.
# Multiple correct letter orders may exist, and returning any one of them is considered acceptable.
# Let's demonstrate this with an example for better understanding:

# 1
# 2plaintext
# 3Input: ["wrt", "wrf", "er", "ett", "rftt"]
# 4Output: "wertf"
# 5
# 6In this example, we can see how the order of the letters 't, e, w, r, f' came to be.
# 7
# 8- "wrt" and "wrf" show 't' comes before 'f'.
# 9- "wrf" and "er" imply 'w' is followed by 'e'.
# 10- "er" and "ett" give us 'e' preceding 'r'.
# 11- "ett" and "rftt" suggest 't' comes before 'r'.
# The rules we inferred culminate in the order 'wertf'. The example clued us into a possible solution strategy: comparing consecutive words and adding dependencies.

# The problem is effectively a topological sorting problem, and it makes use of the concept of directed graphs. To satisfy the requirements, we use BFS (Breadth-First Search) algorithm to solve this problem. The steps followed are:

# We first create a graph to note the dependencies between characters. For each consecutive pair of words, we look for the first position where the letters differ, and then the first letter would be a parent in the graph (that should come first), the second one is a child (that should come after its parent).
# We also keep a count of the indegree for all dependant nodes (children) in the graph.
# After we completed processing all the words and capturing all dependencies in the graph, we run BFS on it, and the queue should first have nodes with 0 indegree. For each node we added to the queue, we decrease the indegree of its children as we've "sorted" its parent.
# As we dequeue each node, we add it to the answer string.
# Finally, we only return the result if all characters in the graph are included in the result, otherwise, we return an empty string, which means there's a cycle in the graph.


from typing import List
import collections
from collections import defaultdict
import heapq
from collections import deque
from collections import Counter
def alien_order(words: List[List[str]]) -> str:
    adj_list=defaultdict(set)
    in_degree=Counter({c :0 for word in words for c in word})
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word):
            if c !=d:
                if d not in adj_list[c]:
                    adj_list[c].add[d]
                    in_degree[d]+=1
                break
            else:
                if len(second_word) < len(first_word):
                    return ""
    output=[]
    queue=deque([c for c in in_degree if in_degree[c]==0])
    while queue:
        c=queue.popleft()
        output.append(c)
        for d in adj_list[c]:
            in_degree[d] -=1
            if in_degree[d] ==0:
                queue.append(d)
    if len(output) < len(in_degree):
        return ""
    return "".join(output)
if __name__ == "__main__":
    words=["wrt", "wrf", "er", "ett", "rftt"]
    print ("{}".format(alien_order(words)))



