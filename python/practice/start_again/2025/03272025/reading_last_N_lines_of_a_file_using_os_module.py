#   https://www.geeksforgeeks.org/python-reading-last-n-lines-of-a-file/

import os 
def LastNLines(fname, N):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    iter = 0 
    with open(fname) as f :
        if bufsize > fsize:
            bufsize = fsize -1
            fetched_line = []
            while True:
                iter +=1 
                f.seek(fsize-bufsize * iter)
                fetched_line.extend(f.readlines())
                if len(fetched_line) >= N or f.tell() == 0 :
                    print (''.join(fetched_line[-N:]))
                    break
if __name__ == "__main__":
    fname = 'file.txt'
    N = 3 
    try:
        LastNLines(fname, N)
    except:
        print ('File not found')
