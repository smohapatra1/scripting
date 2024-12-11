#   https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/

def ValidateEmail(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    valid = re.match(regex, email)
    if valid:
        print ("Valid email address ")
    else:
        print ("Invalid email address")

if __name__ == "__main__":
    email = "my.ownsite@our-earth.org"
    ValidateEmail(email)