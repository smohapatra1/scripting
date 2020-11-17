#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
def doll(a):
    var = ''
    for i in a :
        var +=i*3
    print (var)
doll('Samarendra')