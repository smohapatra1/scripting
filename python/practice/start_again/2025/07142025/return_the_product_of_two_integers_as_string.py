#   Return the product of the two integers represented as strings.  

#   https://www.google.com/search?q=Given+are+the+10+activities+with+their+start+and+end+times.+Compute+a+schedule+where+the+greatest+number+of+activities+take+place.+using+python%C2%A0&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifNxNflLsIVF2YdFyK1FNgrmbgPdNw%3A1751840752818&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIemkjk18Cn72Gp24fGkjjh6xc8y8oU3IJovU34XDyOFvEl9PQhCX-bXyx8AzQGU_JUmd7tO0Sp0t0qHqXwx4ZXWb8MG9UW3YmmJ7jnOpDFf7zDe6R0ySzsMzPcR5ELTvwcb0SbmEtrZ6i8BL_Ll7e2CjCTkfGrqQV0WeCBxGgvYCvX7WS9g&aep=1&ntc=1&sa=X&ved=2ahUKEwjSkJmuo6mOAxVDlu4BHRRqCWMQ2J8OegQIFhAC&biw=1729&bih=876&dpr=2&mstk=AUtExfAnh4GP1DD4aNrCcZJYZR0wlfA951kT-T4UFHOP41Gw2o4RA3eI2f1s7Ee1Tl8NlFDD1PEKuY5Ol2xIAM-d2oonc56czFy4e1ywgT2FlzN-RSpiCnWFkmBY0MfFgpAdC2GuNJzVMRwG_6gg94sxXVguqN1cv83iRmjYUnHTBnVuPh4wFoknwlZGzLb2tY8s1TGpKMQ2euvzM97GtdJBJaV0gzpxWWsrHLkyQAPJGv_kec_GTvuKq9Zo6ilHZ5_ijlzgIAaM3CaNR0Z6IlOvKBr948NI63Ua1QBT3upnkP5VpYdnbfmi5h5IACwxaW12_LHRF99jXfEErg&csuir=1


def convert_multiplication_into_string(str1, str2):
    num1 = int(str1)
    num2 = int(str2)
    product = num1 * num2
    return  str(product)

string1 = "123"
string2 = "45"
result = convert_multiplication_into_string(string1, string2)
print(f"The product of {string1} and {string2} is: {result}") # Output: 5535
