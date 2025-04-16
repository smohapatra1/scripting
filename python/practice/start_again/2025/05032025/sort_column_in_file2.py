#   https://www.geeksforgeeks.org/how-to-sort-column-in-a-file-using-python/

def my_sort(line): 
    flight_class = {'ECONOMY': 1, 
                    'PREMIUMECONOMY': 2, 
                    'BUSINESS': 3, 
                    'FIRSTCLASS': 4} 
    line_fields = line.strip().split() 
    cabin_class = line_fields[-1] 
    return flight_class[cabin_class] 
fp = open('file.txt') 
contents = fp.readlines() 
contents.sort(key=my_sort) 
for line in contents: 
    print(line) 
  
fp.close() 