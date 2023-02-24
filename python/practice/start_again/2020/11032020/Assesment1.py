#Use for, .split(), and if to create a Statement that will print out words that start with 's':
#st = 'Print only the words that start with s in this sentence'
st = 'Sam Print only the words that start with s in this sentence'
#print (st.split())
for w in st.split():
    if w[0] == 's' or w[0] == 'S':
        print (w)
#Method2
for w in st.split():
    if w[0].lower() == 's':
        print (w)