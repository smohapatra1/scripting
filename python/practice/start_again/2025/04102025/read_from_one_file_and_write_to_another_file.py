#   https://www.geeksforgeeks.org/read-content-from-one-file-and-write-it-into-another-file/

with open ("gfg input file.txt", "r") as input:
    with open("gfg output file.txt", 'w') as output:
        for line in input:
            output.write(line)
