#   https://www.geeksforgeeks.org/dsa/converting-decimal-number-lying-between-1-to-3999-to-roman-numerals/
def to_roman(x):
    base = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    res = ""
    i = len(base) -1
    while x>0:
        div = x//base[i]
        while div:
            res += sym[i]
            div -= 1
        x %= base[i]
        i -= 1
    return res


x = 3567
print (to_roman(x))