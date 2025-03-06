#   https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/

from fileinput import FileInput

def replacetext(searched, replaced):
    with FileInput('/Users/smohapatra/Documents/Personal/git_workspace/samar/scripting/python/practice/start_again/2025/03212025/file.txt', inplace=True , backup='.bak') as f:
        for line in  f:
            print (line.replace(searched, replaced), end='')
    return "Text Replaced"

if __name__ == "__main__":
    searched = 'place'
    replaced = 'home'
    print (replacetext(searched, replaced))