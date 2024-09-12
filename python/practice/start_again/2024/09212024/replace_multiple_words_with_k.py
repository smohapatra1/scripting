#   https://www.geeksforgeeks.org/python-replace-multiple-words-with-k/?ref=leftbar-rightbar

def ReplaceMultiple(test_str, word_list, repl_word):
    res = ' '.join([repl_word if idx in word_list else idx for idx in test_str.split()])
    return res

if __name__ == "__main__":
    test_str = 'Geeksforgeeks is best for geeks and CS'
    word_list = ["best", 'CS', 'for']
    repl_word = 'gfg'
    result = ReplaceMultiple(test_str, word_list, repl_word)
    print (result)