#   https://www.geeksforgeeks.org/scraping-and-finding-ordered-words-in-a-dictionary-using-python/

import requests
def getWords(): 
  
    # contains about 2500 words 
    url = "http://www.puzzlers.org/pub/wordlists/unixdict.txt"
    fetchData = requests.get(url) 
  
    # extracts the content of the webpage 
    wordList = fetchData.content 
  
    # decodes the UTF-8 encoded text and splits the  
    # string to turn it into a list of words 
    wordList = wordList.decode("utf-8").split() 
  
    return wordList 
  
  
# function to determine whether a word is ordered or not 
def isOrdered(input): 
  
    # fetching the wordList 
    collection = getWords() 
  
    # since the first few of the elements of the  
    # dictionary are numbers, getting rid of those 
    # numbers by slicing off the first 17 elements 
    collection = collection[16:] 
    word = '' 
  
    for word in collection: 
        result = 'Word is ordered'
        i = 0
        l = len(word) - 1
  
        if (len(word) < 3): # skips the 1 and 2 lettered strings 
            continue
  
        # traverses through all characters of the word in pairs 
        while i < l:          
            if (ord(word[i]) > ord(word[i+1])): 
                result = 'Word is not ordered'
                break
            else: 
                i += 1
  
        # only printing the ordered words 
        if (result == 'Word is ordered'): 
            print(word,': ',result) 
  
  
# execute isOrdered() function 
if __name__ == '__main__': 
    input = 'aau'
    print ("Result : ", isOrdered(input))