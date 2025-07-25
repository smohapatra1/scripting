#   https://www.geeksforgeeks.org/python/inventory-management-with-json-in-python/

def display_data():
    import pandas as pd
    import json 
    fd = open('data.json', 'r')
    txt = fd.read()
    data = json.loads(txt)
    fd.close()
    print("Enter '0' To Display Data Category Wise or '1' \
    To Show Data As its Sequence Of Insertion :- ")
    n = int(input())
    if (n==1):
        table = pd.DataFrame(
            columns = ['ID', 'name', 'price', 'category', 'quantity', 'date']
        )
        for i in data.keys():
            temp = pd.DataFrame(columns=['ID'])
            temp['ID'] = [i]
            for j in data[i].keys():
                temp[j] = [data[i][j]]
            table = table.append(temp)
        table = table.reset_index(drop=True)
        from IPython.display import display
        display(table)
    elif (n ==0):
        table = pd.DataFrame(
            columns=['ID', 'name', 'price', 'category', 
                     'quantity', 'date'])
        cat = []
        for i in data.keys():
            temp = pd.DataFrame(columns=['ID'])
            temp['ID'] = [i]
            for j in data[i].keys():
                temp[j] = [data[i][j]]
                if (j == 'category'):
                    cat.append(data[i][j])
            table = table.append(temp)
            table = table.reset_index(drop=True)
            cat = set(cat)
            cat = list(cat)
            
        for k in cat:
            temp = pd.DataFrame()
            temp = table[table['category'] == k]
            print("Data Of Products Of Category "+k+" is:- ")
            from IPython.display import display
            display(temp)
    else:
        print("Enter Valid Choice...!!!")
