#   Rearrange the given string of alphabets in sorted order and all the integers present in the string. 

#   https://www.google.com/search?q=Given+are+the+10+activities+with+their+start+and+end+times.+Compute+a+schedule+where+the+greatest+number+of+activities+take+place.+using+python%C2%A0&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifNxNflLsIVF2YdFyK1FNgrmbgPdNw%3A1751840752818&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIemkjk18Cn72Gp24fGkjjh6xc8y8oU3IJovU34XDyOFvEl9PQhCX-bXyx8AzQGU_JUmd7tO0Sp0t0qHqXwx4ZXWb8MG9UW3YmmJ7jnOpDFf7zDe6R0ySzsMzPcR5ELTvwcb0SbmEtrZ6i8BL_Ll7e2CjCTkfGrqQV0WeCBxGgvYCvX7WS9g&aep=1&ntc=1&sa=X&ved=2ahUKEwjSkJmuo6mOAxVDlu4BHRRqCWMQ2J8OegQIFhAC&biw=1729&bih=876&dpr=2&mstk=AUtExfBvVQnQ6NkSEdAnSiEM4E4iiOwLkbss0Q0prFjy3ZxdmntemVdDhu3wq-hE2Hsia9kVKq5skLFQ7smlJNzpzg8JJBzbqt2QcZ_fkCX4rt87Yua4vQrpODdn4FD_1UVDZ2sw1fqZkeZhhXV15POrtITvicvyqqS9uXCLSs43urbtqYKVGLwjgf2XiAWa6gt31RN6yDrIaJaBAsts2mxUQ4BOjyQhzxOt6HzsWLOgnDM7-3LlTPFsfR_hxjIm-mUvSl3BWW-xbfnCHX2SBVZi7ZatAky1iUgheJpWu0V_JGgGPnIB2wLUBE_-EgiEXTNHEf8_uNd5PWYl4Q&csuir=1

def rearrange_strings_sorted(input_string):
    letters = []
    numbers = []
    for char in input_string:
        if char.isalpha():
            letters.append(char)
        elif char.isdigit():
            numbers.append(int(char))
    sorted_letters = sorted(letters)
    sorted_numbers = sorted(numbers)
    sorted_num_str = [str(num) for num in sorted_numbers]
    result = "".join(sorted_letters) + "".join(sorted_num_str)
    return result

input_str = "a1b2c3"
output_str = rearrange_strings_sorted(input_str)
print (f"Original String : {input_str}")
print (f"Rearrange String : {output_str}")
input_str_2 = "helloWorld1234"
output_str_2 = rearrange_strings_sorted(input_str_2)
print(f"Original string: {input_str_2}")
print(f"Rearranged string: {output_str_2}")