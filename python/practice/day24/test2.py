# Python3 program to convert seconds 
# into days, hours, minutes, seconds 
  
# Function convert second into day  
# hours, minutes and seconds 
def ConvertSectoDay(n): 
  
    day = n // (24 * 3600) 
  
    n = n % (24 * 3600) 
    hour = n // 3600
  
    n %= 3600
    minutes = n // 60
  
    n %= 60
    seconds = n 
      
    print(day,"days", hour, "hours",  
          minutes, "minutes", 
          seconds, "seconds") 
  
  
# Driver code  
  
# Given n is in seconds 
n = 369121517
ConvertSectoDay(n) 
  
# This code is contributed by Anant Agarwal. 
