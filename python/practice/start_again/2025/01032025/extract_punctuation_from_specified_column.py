#   https://www.geeksforgeeks.org/extract-punctuation-from-the-specified-column-of-dataframe-using-regex/

import pandas as pd
import re

df = pd.DataFrame(
    {
        'Name' : ['Akash', 'Ashish', 'Ayush', 
              'Diksha' , 'Radhika'], 
    
        'Comments': ['Hey! Akash how r u' ,  
                    'Why are you asking this to me?' , 
                    'Today, what we are going to do.' , 
                    'No plans for today why?' , 
                    'Wedding plans, what are you saying?']
    },
    columns = ['Name', 'Comments'] 
)
df