#   Can you rotate the given square matrix by 90 degrees in a clockwise direction? The transformation should be done in quadratic time and in-place.

#   https://www.google.com/search?q=Given+are+the+10+activities+with+their+start+and+end+times.+Compute+a+schedule+where+the+greatest+number+of+activities+take+place.+using+python%C2%A0&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifNxNflLsIVF2YdFyK1FNgrmbgPdNw%3A1751840752818&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIemkjk18Cn72Gp24fGkjjh6xc8y8oU3IJovU34XDyOFvEl9PQhCX-bXyx8AzQGU_JUmd7tO0Sp0t0qHqXwx4ZXWb8MG9UW3YmmJ7jnOpDFf7zDe6R0ySzsMzPcR5ELTvwcb0SbmEtrZ6i8BL_Ll7e2CjCTkfGrqQV0WeCBxGgvYCvX7WS9g&aep=1&ntc=1&sa=X&ved=2ahUKEwjSkJmuo6mOAxVDlu4BHRRqCWMQ2J8OegQIFhAC&biw=1729&bih=876&dpr=2&mstk=AUtExfB04Q_QBdOagjox40ibIOv22FgnBMoVWOr9b9ie2ZzdKFQNSbtVzQKIHZTPasJZM_VSwI2JqRppfWwpgQceiAvDntnXdZPpj6V4hj9-OTuhQD38TY6bTgRDrVmL7Fmf6YZ8mUA4YwWsACOmLOw4m8EQ5gh-PRpvmRa7Sg2LTqXlm64dxO1O8bkDZoPI1XkdZ9ZS21u_v9MWFKGsk4Yl1JU-t7ghICCsCjjUqhuOJGsJSoJvKOkqp7ut7pg8fDMshE_gj9lpMQZAVJhKkN71ZQsbl2aKpWmO42xdZKlXoS30Zam-Vzry6_ahfgObyqloZCVaoDC70kK1eQ&csuir=1

def rotate_90_degrees(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n ):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print ("Original Matrix 1: ")

for row in matrix1:
    print (row)

rotate_90_degrees(matrix1)

print("\nRotated Matrix 1 (90 degrees clockwise in-place):")
for row in matrix1:
  print(row)

print("\n" + "="*30 + "\n")