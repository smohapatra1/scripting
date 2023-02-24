with open('test.txt', mode='w+') as f:
    f.write('\n Hello World')
    f.close()
    print (f.read())
