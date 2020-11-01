#Dictionary 
books={'k1': 10.00, 'k2': [0,1,2], 'k3': {'Key1': ['sama']}}
print (books['k1'])
print (books['k3']['Key1'])
#Insert a new value 
books['k1'] = 100
print (books)
books['k1'] = 'NEW VALUE'
print (books)
#print keys 
print ('All Keys are {}'.format(books.keys()))
print ('All Values are {}'.format(books.values()))
print ('All Items are {}'.format(books.items()))
d={'k1':[1,2,3]}
print (d['k1'][1])
