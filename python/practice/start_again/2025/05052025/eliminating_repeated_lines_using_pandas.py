#   https://www.geeksforgeeks.org/eliminating-repeated-lines-from-a-file-using-python/

import pandas as pd

def remove_duplicate(f1, f2):
    df = pd.read_csv(f1, header=None)
    df.drop_duplicates(inplace=True)
    df.to_csv(f2, header=False, index= False)

f2 = open('file.txt', 'w')

f1 = open('file2.txt', 'r')
remove_duplicate(f1, f2)