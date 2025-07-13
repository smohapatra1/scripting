#   You are given integers in the form of an array. How will you print the largest subarray sum having at least K numbers?

#   https://www.google.com/search?q=Given+are+the+10+activities+with+their+start+and+end+times.+Compute+a+schedule+where+the+greatest+number+of+activities+take+place.+using+python%C2%A0&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifNxNflLsIVF2YdFyK1FNgrmbgPdNw%3A1751840752818&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIemkjk18Cn72Gp24fGkjjh6xc8y8oU3IJovU34XDyOFvEl9PQhCX-bXyx8AzQGU_JUmd7tO0Sp0t0qHqXwx4ZXWb8MG9UW3YmmJ7jnOpDFf7zDe6R0ySzsMzPcR5ELTvwcb0SbmEtrZ6i8BL_Ll7e2CjCTkfGrqQV0WeCBxGgvYCvX7WS9g&aep=1&ntc=1&sa=X&ved=2ahUKEwjSkJmuo6mOAxVDlu4BHRRqCWMQ2J8OegQIFhAC&biw=1729&bih=876&dpr=2&mstk=AUtExfDO9jkFKj-5thE4Rr7SCP9bhUtJ7Kc4Fpeibl51h4RRTtbiUPLrTvIAPzYA7-wDltNKZUc1DJepejTDiXvcgulib5G4NAbYMOlmqHHMi4qn4PSicM8AzHXVrH7QHTh8uIDRwVR0xXj78WlVdR0O64PpOnb0w3BO2psYT8LjO2wIeJ-V-UdDdUDYhbRc2sSNNXjAczJpCtYYDYjZBiJAq0Defwrs7bQ0PVyOHzwxMMzQXsQuTsuGWwo6AiLDKjg7mhrDrunHOH5hMaHDuRbKFloPtOySYsriTmQniNal3bA-w9Z0ruz2fwdqDFy3VUjpS_rJwwRa7w9LKg&csuir=1

def max_subarray_sum(arr, k ):
    n = len(arr)
    if n < k :
        return 0 
    max_so_far = arr[0]
    current_max = arr[0]
    max_sum_ending_at_i = [0] * n 
    max_sum_ending_at_i[0] = arr[0]
    for i in range(1, n ):
        current_max = max(arr[i], current_max + arr[i])
        max_sum_ending_at_i[i] = current_max
        max_so_far = max(max_so_far, current_max)
    current_window_sum = sum(arr[:k])
    max_total_sum = current_window_sum
    for i in range(k, n ):
        current_window_sum += arr[i] - arr[i-k]
        max_total_sum = max(max_total_sum, current_window_sum)
        max_total_sum = max(max_total_sum, current_window_sum + max_sum_ending_at_i[i-k])
    return max_total_sum
arr1 = [1, -2, 3, -1, 2, -5, 4]
k1 = 3
print(f"Array: {arr1}, K: {k1}, Largest Subarray Sum: {max_subarray_sum(arr1, k1)}") # Output: 5 (subarray [3, -1, 2, -5, 4] is 3; [3, -1, 2] is 4; [1, -2, 3, -1, 2] is 3. Max is 5)
