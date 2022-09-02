#Enter your email - If its invalid show user to enter valid email
# Show username and domains differently

def email():
    addr=input("Enter your email address: ")
    index=addr.find('@')
    if index == -1:
        print ("Enter a valid email address ")
    else:
        print (f"Domain is  : ", addr[index+1:])
        print ("Username is : ", addr[:index])

email()