#Palindrone problem 
#radar = > radar
#madam=> madam

from tracemalloc import start


def palindrone(a):
    original_string=a
    reverse_string=reverse(a)

    if original_string == reverse_string:
        #return True
        print (f"{a} is palindrone")
    else:
        print (f"{a} is not palindrone")
    #return False
    
def reverse(a):
    a = list(a)
    print (a)
    start_num=0
    end_num=len(a) -1
    while end_num > start_num:
        a[start_num], a[end_num] = a[end_num], a[start_num]
        start_num +=1
        end_num-=1
      
    return ''.join(a)


if __name__ == '__main__':
    a=input("Enter a staing : ")
    #a = [ 's', 'a', 'm', 'a' , 'r' ]
    palindrone(a)
    #print (a)
