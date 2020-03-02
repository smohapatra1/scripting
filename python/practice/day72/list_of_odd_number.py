def _list_of_odd_numbers_sample_(a, b):
    output_list = []
    number = b
    while number >= a:
        if number % 2 != 0:
            output_list.append(number)
        number = number - 1
    #return output_list
    print (output_list)
_list_of_odd_numbers_sample_(11, 31)
