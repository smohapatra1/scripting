#   https://www.geeksforgeeks.org/how-to-remove-repetitive-characters-from-words-of-the-given-pandas-dataframe-using-regex/

import pandas as pd
import re

df = pd.DataFrame(
    {
        'name' : ['Akash', 'Ayush', 'Diksha',
            'Priyanka', 'Radhika'],
    
        'common_comments' : ['hey buddy meet me today ',
                        'sorry bro i cant meet',
                        'hey akash i love geeksforgeeks',
                        'twiiter is the best way to comment',
                        'geeksforgeeks is good for learners']
    },
    columns = ['name', 'common_comments']
)
df