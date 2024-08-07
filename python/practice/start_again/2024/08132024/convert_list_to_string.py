#   Converting a List into a String

def convertString(days):
    lost = ' '.join(days)
    print (lost)
if __name__ == "__main__":
    days = ['S','M','T','W','Tr','F','St']
    result = convertString(days)
