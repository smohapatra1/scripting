#Write a function that takes a string and returns matching string where every even letter is uppercase
# and every odd letter is lowercase 

def skyline(**kwargs):
    for i in kwargs:
        out = ''
        print (len(i))
        if len(i) % 2 == 0 :
            print (out.append(kwargs[i].upper()))
        else:
            print ("Letter is Odd {}".format (i))
skyline(letter1 = "Samar", letter2 = "Sa", lett = "Sama")