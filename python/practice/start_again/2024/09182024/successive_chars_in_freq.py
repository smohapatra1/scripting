#   https://www.geeksforgeeks.org/python-successive-characters-frequency/
import re 

def Successive(test_str, que_word):
    temp = []
    for sub in re.findall(que_word + '.', test_str):
        temp.append(sub[-1])
    res = {que_word : temp.count(que_word) for que_word in temp}
    return res

if __name__ == "__main__":
    test_str = 'geeksforgeeks is best for geeks. A geek should take interest.'
    que_word = "geek"
    result = Successive(test_str, que_word)
    print (result)