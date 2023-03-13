#Given two tuples called tuple1 and tuple2, perform the operations described in comments in the editor.
def main():
    tuple1 = tuple(("one", "two", "three"))
    tuple2 = tuple(("1", "2", "3"))
    
    # change value at index 0 of both tuple to string "number"
    # Your code goes here
    tuple1=list(tuple1)
    tuple2=list(tuple2)
    tuple1[0]= "number"
    tuple2[0]= "number"
    
    print(tuple1)
    print(tuple2)
    my_tuple1 = ('one', 'two', 'three')
    my_tuple2 = ('1', '2', '3')
    my_tuple3 = my_tuple1 + my_tuple2
    print(my_tuple3)
    return 0

if __name__ == '__main__':
    main()