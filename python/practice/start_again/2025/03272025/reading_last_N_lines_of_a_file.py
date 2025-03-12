#   https://www.geeksforgeeks.org/python-reading-last-n-lines-of-a-file/

def LastNlines(fname, N):
    with open(fname) as file:
        for line in (file.readlines() [-N:]):
            print(line, end ='')

if __name__ == '__main__':
    fname = 'file.txt'
    N = 2
    try:
        LastNlines(fname, N)
    except:
        print('File not found')