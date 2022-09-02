#Enter an email address and filter out domain and username 

def email():
    email=input("Enter email address : ")
    index=email.find('@')
    if index == -1 :
        print ("Enter a valid email")
    else:
        print("Username is : ",email[:index])
        print("Domain   is : ",email[index+1:])
email()
