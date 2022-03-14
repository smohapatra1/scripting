#Find if a number is divisible by 5 or 8
def is_divisibale_by_5_or_8(n):
    def divisible_by_5(n):
        if n % 5 == 0:
            return True
        else:
            return False
    def divisible_by_8(n):
        if n % 8 == 0:
            return True
        else:
            return False
    if divisible_by_5(n) and divisible_by_8(n):
        print (f'{n} is divisible by 5 and 8 ')
    else:
        print (f'{n} is not divisible by 5 and 8')
        #return False
is_divisibale_by_5_or_8 (80)