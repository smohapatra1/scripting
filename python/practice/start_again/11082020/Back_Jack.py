
#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
#return their sum. If their sum exceeds 21 and there's an eleven, 
#reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19
def jack(a,b,c):
    if sum([a,b,c]) <= 21:
        print ("Sum : {}".format(sum([a,b,c])))
    elif 11 in [a,b,c] and sum([a,b,c]) <=31:
        print ("Sum2 = {}".format(sum([a,b,c]) - 10))
    else:
        print ("BUST")
jack(9,10,9)