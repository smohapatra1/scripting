#   https://www.geeksforgeeks.org/python-program-to-print-lines-containing-given-string-in-file/


# file_name = ('file.txt', 'r')

try :
    file_read = open('file.txt', 'r')
    text = input('Enter the string : ')
    lines = file_read.readlines()
    new_list = []
    idx = 0 
    for line in lines:
        if text in line:
            new_list.insert(idx, line)
            idx +=1
    file_read.close()
    if len(new_list == 0):
        print ("\n\"" +text+ "\" is not found in \"" +file_read+ "\"!")
    else:
        lineLen = len(new_list)
        print ("\n**** Lines containing \"" +text+ "\" ****\n")
        for i in range(lineLen):
            print (end=new_list[i])
        print ()
except :
    print ("\n The file doesn't exist!")


