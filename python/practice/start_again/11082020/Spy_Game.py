#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False
def spy(arr):
    first_letter = [0,0,7,'x']
    for i in arr:
        if i == first_letter[0]:
            first_letter.pop(0)
            print ("y {}".format(i))
        
spy([1,7,2,0,4,5,0])