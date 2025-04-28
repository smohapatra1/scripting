#   https://www.geeksforgeeks.org/open-a-file-by-regular-expression-in-python/

import re

def open_file_by_regex(file_pattern):
    # List all files in the current directory
    files = ["example.txt", "data.csv", "report.docx", "image.png"]

    # Use regex to match files based on the provided pattern
    pattern = re.compile(file_pattern)
    matching_files = [file for file in files if pattern.search(file)]

    # Open and print the content of each matching file
    for file_name in matching_files:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of {file_name}:\n{content}\n")

# Example usage
open_file_by_regex(r'.*\.txt')