#MASTER YODA: Given a sentence, return a sentence with the words reversed
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'
def yoda(a):
    #Split the word 
    l=a.split()
    reverse_list=l[::-1]
    #Join method
    print (' '.join(reverse_list))
yoda("I love papapa and mama")