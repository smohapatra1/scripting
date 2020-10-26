#Use print Format
string="Hello"
print('Hello {} {}' .format('Samar' ,' , How are you?'))
# Another format of replacing indexes/formats 
print('Hello {1} {0}' .format('Samar' ,' , How are you?'))
#Using key value pairs 
print ('Hello {a} {b}'.format(a='Samar,', b='How are you?'))  
result = 100/777
print ('Your result is {r}'.format(r=result))
#Format values - "value:width.percision f""
print ('Your result is {r:1.3f}'.format(r=result))
#Formatted string
name="samar"
print(f'My name is {name}')
print('Python {} {} {}'.format('rules!', 'and', 'rocks'))
