#   https://www.geeksforgeeks.org/problems/if-loop-python/1

def FriendAngry(j_angry, s_angry):
    if j_angry == s_angry:
        return 'True'
    else:
        return 'False'

if __name__ == "__main__":
    j_angry = 'True'
    s_angry = 'True'
    print ("Both and Angry ? ", FriendAngry(j_angry, s_angry))