# https://stackoverflow.com/questions/69802052/how-to-write-the-program-that-prints-out-all-positive-integers-between-1-and-giv

num = int(input("Please type in a number: "))
number_list = [i+1 for i in range(num)]

while number_list:
    print(number_list.pop(0))
    number_list.reverse()