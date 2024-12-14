#   https://www.geeksforgeeks.org/how-to-extract-date-from-excel-file-using-pandas/

import pandas as pd
import re

data = pd.read_excel("test.xlsx")
print ("Original Data")
data