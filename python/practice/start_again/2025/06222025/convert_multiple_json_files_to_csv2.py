#   https://www.geeksforgeeks.org/python/convert-multiple-json-files-to-csv-python/

import pandas as pd

df1 = pd.read_json('file.json')
print (df1)
df2 = pd.read_json('file3.json')
print (df2)

df_inner = pd.merge(df1, df2, how='inner', left_on=[
                    'ID', 'Name'], right_on=['ID', 'Name'])
df_outer = pd.merge(df1, df2, how='outer', left_on=[
                    'ID', 'Name'], right_on=['ID', 'Name'])
df_left = pd.merge(df1, df2, how='left', left_on=[
                   'ID', 'Name'], right_on=['ID', 'Name'])
df_right = pd.merge(df1, df2, how='right', left_on=[
                    'ID', 'Name'], right_on=['ID', 'Name'])
df_inner.to_csv("CSV_inner.csv", index=False)
df_outer.to_csv("CSV_outer.csv", index=False)
df_left.to_csv("CSV_left.csv", index=False)
df_right.to_csv("CSV_right.csv", index=False)

result_inner = pd.read_csv("CSV_inner.csv")
result_outer = pd.read_csv("CSV_outer.csv")
result_left = pd.read_csv("CSV_left.csv")
result_right = pd.read_csv("CSV_right.csv")
print ("result_inner")
print ("result_outer")
print ("result_left")
print ("result_right")