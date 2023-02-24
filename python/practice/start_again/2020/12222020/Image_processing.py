from PIL import Image 
mac = Image.open('search.jpg')
print ("Filename  : ", mac.filename)
print ("File Details :  ", mac.format_description)
print ("File Size : ", mac.size)
