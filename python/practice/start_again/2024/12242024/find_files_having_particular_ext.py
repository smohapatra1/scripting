#   https://www.geeksforgeeks.org/python-program-to-find-files-having-a-particular-extension-using-regex/

# Find the words after .
import re

def FileExtMatch(filenames):
    for file in filenames:
        match = re.search("\.xml$", file)
        if match:
            print ("Has a XML Extensions", file)
        else:
            print ("Doesn't have XML Extensions", file)

if __name__ == "__main__":
    filenames = ["gfg.html", "geeks.xml",  
            "computer.txt", "geeksforgeeks.jpg"]
    FileExtMatch(filenames)
