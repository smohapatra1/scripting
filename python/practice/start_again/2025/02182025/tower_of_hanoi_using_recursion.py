#   https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/

def TowerofHanoi(n, source, destination, auxiliary):
    if n == 1 :
        print ("Move Disk 1 from source ", source, "to desitination", destination)
        return
    TowerofHanoi(n-1, source, auxiliary, destination)
    print ("Move disk", n , "from source", "to destination", destination)
    TowerofHanoi(n-1, auxiliary, destination, source)

n = 4 
TowerofHanoi(n, 'A', 'B', 'C' )