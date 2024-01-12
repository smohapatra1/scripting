# #   https://leetcode.com/problems/excel-sheet-column-title/description/

# 168. Excel Sheet Column Title
# Easy

# Topics
# Companies
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnNumber = 1
# Output: "A"
# Example 2:

# Input: columnNumber = 28
# Output: "AB"
# Example 3:

# Input: columnNumber = 701
# Output: "ZY"

def ExcelColumns(columnNumber : int ) -> str:
    if not columnNumber:
        return ""
    columnNumber, remainder = divmod(columnNumber - 1, 26)
    return ExcelColumns(columnNumber) + chr(65 + remainder)

if __name__ == "__main__":
    columnNumber=701
    print ("{}".format(ExcelColumns(columnNumber)))