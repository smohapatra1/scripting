#   https://www.geeksforgeeks.org/take-input-from-user-and-store-in-txt-file-in-python/

temp = input("Enter your information : ")
try:
    with open('file.txt', 'w') as f:
        f.write(temp)
except Exception as e:
    print ("Error in writing ", str(e))
