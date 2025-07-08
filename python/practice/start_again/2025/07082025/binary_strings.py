#   Given are two strings with binary numbers. Find the result obtained by adding those two binary strings and return the result as a binary string. 

#   https://www.google.com/search?q=Given+are+the+10+activities+with+their+start+and+end+times.+Compute+a+schedule+where+the+greatest+number+of+activities+take+place.+using+python%C2%A0&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifNxNflLsIVF2YdFyK1FNgrmbgPdNw%3A1751840752818&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIemkjk18Cn72Gp24fGkjjh6xc8y8oU3IJovU34XDyOFvEl9PQhCX-bXyx8AzQGU_JUmd7tO0Sp0t0qHqXwx4ZXWb8MG9UW3YmmJ7jnOpDFf7zDe6R0ySzsMzPcR5ELTvwcb0SbmEtrZ6i8BL_Ll7e2CjCTkfGrqQV0WeCBxGgvYCvX7WS9g&aep=1&ntc=1&sa=X&ved=2ahUKEwjSkJmuo6mOAxVDlu4BHRRqCWMQ2J8OegQIFhAC&biw=1729&bih=876&dpr=2&mstk=AUtExfAZAx3b_p_RripER0DIcmoernBU_41892EVpEv_KcV_5VDRh1EaQxIVuTMheZm7wbgpODxToKQ1M9cCeBSucnOPS64NFZNrWfDWdij82Po_7qYivX2XtRieKneZ7uDLfzPAT945P7I0hbBDyZXfWLaFQbmseDP_TWT44Ic5q5a4K3oSX1Jg8fI_qLw6pHPivXgZ9WmYTPNtgebh4BgwvQa8LSWu2mkZIn4JsUSNoygbRLUNRvsgNZP4HLCHfP9sqciZP2O3Xn5fHf5d6fhrW_dC4WN9NW9F4AxMz9avbgumbD64F-1_nqQw9EixaZKydymdrW5P2XDUtg&csuir=1


def add_binary_builtins(a, b ):
    decimal_sum = int(a, 2) + int(b, 2)
    binary_sum = bin(decimal_sum)
    return binary_sum[2:]
a = '11'
b = '1'
result = add_binary_builtins(a, b )
print (f"The Sum of {a} and {b} is : {result}")
a = '1010'
b = '1011'
result = add_binary_builtins(a, b )
print (f"The Sum of {a} and {b} is : {result}")