#   https://www.geeksforgeeks.org/python/inventory-management-with-json-in-python/

def display_data():
    import pandas as pd 
    import json
    fd = open("data.json", 'r')
    txt = fd.read()
    fd.close()
    print ("Enter product ID Whose details you want to Have a look on: - ")
    i = input()
    if i in data.keys():
        temp = pd.DataFrame(columns=['ID'])
        temp['ID'] = [i]
        for j in data[i].keys():
            temp[j] = [data[i][j]]
        from IPython.display import display
        display(temp)
    else:
        print("You Have Entered Wrong Product ID \
        that is not Present in DataBase...!!!")