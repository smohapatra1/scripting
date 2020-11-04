#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
mylist=[w[0] for w in st.split()]
print (mylist)