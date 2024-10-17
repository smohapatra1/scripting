#   https://www.geeksforgeeks.org/dictionary-counter-python-find-winner-election/

from collections import Counter
def Winner(votes):
    Vote_counts = Counter(votes)
    Max_Vote = max(Vote_counts.values())
    res = [i for i in Vote_counts.keys() if Vote_counts[i] == Max_Vote]
    return sorted(res)[0]

if __name__ == "__main__":
    votes =['john','johnny','jackie','johnny','john','jackie',
    'jamie','jamie','john','johnny','jamie','johnny','john'] 
    print ("The Winner is : ", Winner(votes))
