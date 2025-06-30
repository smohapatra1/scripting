#   Calculate the maximum value using the '+' or '*' sign between two numbers in the given string.


def calculate_max_value(s):
    if not s:
        return 0 
    result = int(s[0])
    for i in range(1, len(s)):
        current_digit = int(s[i])
        if result <= 1 or current_digit <=1:
            result += current_digit
        else:
            result *= current_digit
    return result
string1 = "01231"
print(f"Maximum value for '{string1}': {calculate_max_value(string1)}")

string2 = "891"
print(f"Maximum value for '{string2}': {calculate_max_value(string2)}")

string3 = "5012"
print(f"Maximum value for '{string3}': {calculate_max_value(string3)}")
