#   


roman_map = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
    (1, "I")
]
def decimal_to_roman(num):
    if not 1 <= num <=3999:
        raise ValueError("Input must be an integer between 1 and 3999")
    result = ""
    for decimal_value, roman_numeric in roman_map:
        while num >= decimal_value:
            result += roman_numeric
            num -= decimal_value
    return result

print (decimal_to_roman(3749)) 
