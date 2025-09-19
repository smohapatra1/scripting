#   https://www.geeksforgeeks.org/python/convert-a-bytes-array-into-json-format-in-python/

import json 

byte = b'[{\'Date\': \'2016-05-21T21:35:40Z\', \'CreationDate\': \'2012-05-05\',\
    \'LogoType\': \'png\', \'Ref\': 164611595, \'Classe\': [\'Email addresses\', \
    \'Passwords\'],\'Link\':\'http://some_link.com\'}]'
byte = byte.decode().replace("'", '"')
ans = json.loads(byte)
print (ans)