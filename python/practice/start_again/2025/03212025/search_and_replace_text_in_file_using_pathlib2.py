#   https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/

from pathlib import Path

def replacetext(searched, replaced):
    file = Path(r'file.txt')
    data = file.read_text()
    data = data.replace(searched, replaced)
    file.write_text(data)
    return "Text Replaced"





if __name__ == "__main__":
    searched = 'place'
    replaced = 'home'
    print (replacetext(searched, replaced))