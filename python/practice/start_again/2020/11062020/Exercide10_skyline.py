#Write a function that takes a string and returns matching string where every even letter is uppercase
# and every odd letter is lowercase 

def skyline(**kwargs):
    out =[]
    for i in kwargs:
        #print (kwargs[i])
        
        #print (len(kwargs[i]))
        if len(kwargs[i])%2 == 0 :
            print ("Even : ", kwargs[i].upper())
            out.append(kwargs[i].upper())
    #return out
        else:
            print ("ODD : ", kwargs[i].lower())
            out.append(kwargs[i].lower())
    #return ''.join(out)
    return out
    
skyline(letter1 = "Samar", letter2 = "Sa", lett = "Sama",letter5 = 'sam')

