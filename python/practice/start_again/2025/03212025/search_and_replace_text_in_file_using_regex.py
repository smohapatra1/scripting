#   https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/

import re

def replacetext(searched, replaced):
    with open('file.txt', 'r+') as f :
        file = f.read()
        file = re.sub(searched, replaced, file)
        f.seek(0)
        f.write(file)
        f.truncate()
    return "Text replaced"

if __name__ == "__main__":
    searched = 'place'
    replaced = 'home'
    print (replacetext(searched, replaced))