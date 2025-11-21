#   https://www.geeksforgeeks.org/python/taking-screenshots-using-pyscreenshot-in-python/

import pyscreenshot
image = pyscreenshot.grab(bbox=(10,10,500,500))
image.show()
image.save("test2.png")