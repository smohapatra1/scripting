#   State which histogram has the largest rectangular area. Also, return the area of the largest histogram. 

#   https://www.google.com/search?q=Given+are+the+10+activities+with+their+start+and+end+times.+Compute+a+schedule+where+the+greatest+number+of+activities+take+place.+using+python%C2%A0&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifNxNflLsIVF2YdFyK1FNgrmbgPdNw%3A1751840752818&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIemkjk18Cn72Gp24fGkjjh6xc8y8oU3IJovU34XDyOFvEl9PQhCX-bXyx8AzQGU_JUmd7tO0Sp0t0qHqXwx4ZXWb8MG9UW3YmmJ7jnOpDFf7zDe6R0ySzsMzPcR5ELTvwcb0SbmEtrZ6i8BL_Ll7e2CjCTkfGrqQV0WeCBxGgvYCvX7WS9g&aep=1&ntc=1&sa=X&ved=2ahUKEwjSkJmuo6mOAxVDlu4BHRRqCWMQ2J8OegQIFhAC&biw=1729&bih=876&dpr=2&mstk=AUtExfCzrsTkhh9pWSFZm4ayUUlboNZ7jhOXX2UorpaSCYT998VGSRdz1fYxTuKX5nBJ4W5Ww_b0SPZjcQmhsBz8Esh9pqGQTW8BcT2VL2Bzd2tF6OMHSvooJYgRkYMUDfzpnriPFXK2Iw8sQXqp25LZfpeguvHRp6xSMc_gA6Y26o2dpZp60PJCpWlmJl-ctWLjnUnbJ2gLpxBSQllq0EzkZD5VgpxOO50xRscXI6AGfYWQzDOjX5CPDKR0b_46U562d2tecoIIKHZDG6UGCt6UXHv4Kosm3-Nkvu8VskJh-P531rRQyvylYQEIXKNNojD855sgSLTzEtGvVA&csuir=1

def largest_rectangle_area(heights):
    stack = []
    max_area = 0 
    heights.append(0)
    for i, height in enumerate(heights):
        start_index = i
        while stack and stack[-1][1] > height:
            index , h = stack.pop()
            width = i - index
            current_area = h * width
            max_area = max(max_area, current_area)
            start_index = index
        stack.append((start_index, height))
    return max_area

heights = [2, 1, 5, 6, 2, 3]
result = largest_rectangle_area(heights)
print (f"Histogram : {heights[:-1]}")
print (f"Largest Rectangle Area : {result}")


