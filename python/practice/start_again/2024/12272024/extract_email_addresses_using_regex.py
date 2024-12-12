#   https://www.geeksforgeeks.org/extracting-email-addresses-using-regular-expressions-python/

def ValidEmail(s):
    print (re.findall('\S+@\S+', s))

if __name__ == "__main__":
    s = "Hello s1231244@gmail.com xyz abc@gmail.com"
    ValidEmail(s)