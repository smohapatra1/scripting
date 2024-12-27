import math

def my_sqrt(input_number):
    srt = input_number/2
    accuracy = 0.001
    while abs(input_number - (srt ** 2)) > accuracy:
            srt = ( srt + (input_number/srt))/2
            return srt
for x in range(1,21):
    y = my_sqrt(x)
    print ("Square root of " , x , "is ",  y )

