#   https://www.geeksforgeeks.org/eliminating-repeated-lines-from-a-file-using-python/

def remove_repeated(input_file, output_file):
    lines_seen = set()
    with open(output_file, 'w') as f1:
        with open(input_file, 'r') as f2:
            for line in f2:
                if line not in lines_seen:
                    f1.write(line)
                    lines_seen.add(line)
input_file = open('file.txt', "r")
output_file = open('file2.txt', "w")
remove_repeated(input_file, output_file)