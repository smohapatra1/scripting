#   https://www.geeksforgeeks.org/python-reading-last-n-lines-of-a-file/


def LastNLines(fname, N):
    assert N >=0
    pos = N + 1
    lines = []
    with open(fname) as f :
        while len(lines) <= N :
            try: 
                f.seek(-pos, 2)
            except IOError:
                f.seek(0)
                break
            finally:
                lines = list(f)
            pos *= 2
    return lines[-N:]

if __name__ == '__main__':
    fname = 'file.txt'
    N = 4 
    try:
        lines = LastNLines(fname, N)
        for line in lines:
            print (line, end='')
    except:
        print ('File not found')
