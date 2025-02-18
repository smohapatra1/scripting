#   https://www.geeksforgeeks.org/write-a-dictionary-to-a-file-in-python/

details = {'Name' : "Bob",
            'Age' : 28 ,
            'Degree' : "Bachelors",
            'Univ' : 'UCLA'}
with open("file.txt", "w") as f:
    for key, value in details.items():
        f.write('%s:%s\n' % (key, value))