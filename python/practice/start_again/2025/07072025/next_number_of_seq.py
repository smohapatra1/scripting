#   What is the next number of the sequence - 1, 11, 21, 1211…?

#   https://www.google.com/search?q=Given+are+the+10+activities+with+their+start+and+end+times.+Compute+a+schedule+where+the+greatest+number+of+activities+take+place.+using+python%C2%A0&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifNxNflLsIVF2YdFyK1FNgrmbgPdNw%3A1751840752818&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIemkjk18Cn72Gp24fGkjjh6xc8y8oU3IJovU34XDyOFvEl9PQhCX-bXyx8AzQGU_JUmd7tO0Sp0t0qHqXwx4ZXWb8MG9UW3YmmJ7jnOpDFf7zDe6R0ySzsMzPcR5ELTvwcb0SbmEtrZ6i8BL_Ll7e2CjCTkfGrqQV0WeCBxGgvYCvX7WS9g&aep=1&ntc=1&sa=X&ved=2ahUKEwjSkJmuo6mOAxVDlu4BHRRqCWMQ2J8OegQIFhAC&biw=1729&bih=876&dpr=2&mstk=AUtExfADj7_hGl6orJG0OExZr3I7fvMjakc1L7IHm53T-tX0bLDSDn6O_moQ1axdbvcKNN-zL8AK8AZKUjj4lGuMra6d4QNZWxN30x4DnNwf5TCeJY1rNTZccFyWpRLbU0ZaDZ0cekVulSTH2tZqpxY5Qv4Xk6FTK4suaKixQZTAMSh4wHhA8JokWaYigv19k4kdHR5AbD6MYzgsk9yzpBIpRfj3XJW4XXWCg3uC2xc3nwpfpe6JnPVFFBKVMQAeQUmjOHQGKCpVT_iUecoWCs0xljX7dvEIVDT5NSLGMEQ-HTI0rUFZjWcOMz9W97iSt6KbvZ6pDbYmWw-s0w&csuir=1

def look_and_say(n):
    result = ""
    count = 0 
    prev_digit = ""
    for digit in n:
        if digit != prev_digit:
            if count >0 :
                result += str(count) + prev_digit
            prev_digit = digit
            count = 1
        else:
            count += 1
    result += str(count) + prev_digit
    return result

sequence = ["1", "11", "21", "1211"]
for i in range(len(sequence)- 1):
    next_term = look_and_say(sequence[i])
    print (f"The next term after {sequence[i]} is {next_term}")
next_number = look_and_say("1211")
print (f"The next number in the sequence after 1211 is : {next_number}")

