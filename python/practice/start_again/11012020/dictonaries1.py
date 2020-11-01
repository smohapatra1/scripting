#Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
# Grab 'hello'
print ("get hello {}".format(d['simple_key']))

d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print ("Grab hello -Nested : {}".format(d['k1']['k2']))

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
print ( "More nested {}".format(d['k1'][0]['nest_key'][1][0]))

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print ("3rd nested : {}" .format(d['k1'][2]['k2'][1]['tough'][2][0]))

