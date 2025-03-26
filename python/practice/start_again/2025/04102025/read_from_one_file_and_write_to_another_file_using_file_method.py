#   https://www.geeksforgeeks.org/read-content-from-one-file-and-write-it-into-another-file/

output_file = open("gfg output file.txt", 'w')
with open("gfg input file.txt", "r") as f:
    output_file.write(f.read())
output_file.close()