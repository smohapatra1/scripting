#   Map the digits of the given positive number corresponding to the alphabet in the mapping table. Also, return the count of the total number of decodings possible. Take suitable assumptions before coding.

#   https://www.google.com/search?q=Given+are+the+10+activities+with+their+start+and+end+times.+Compute+a+schedule+where+the+greatest+number+of+activities+take+place.+using+python%C2%A0&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifNxNflLsIVF2YdFyK1FNgrmbgPdNw%3A1751840752818&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIemkjk18Cn72Gp24fGkjjh6xc8y8oU3IJovU34XDyOFvEl9PQhCX-bXyx8AzQGU_JUmd7tO0Sp0t0qHqXwx4ZXWb8MG9UW3YmmJ7jnOpDFf7zDe6R0ySzsMzPcR5ELTvwcb0SbmEtrZ6i8BL_Ll7e2CjCTkfGrqQV0WeCBxGgvYCvX7WS9g&aep=1&ntc=1&sa=X&ved=2ahUKEwjSkJmuo6mOAxVDlu4BHRRqCWMQ2J8OegQIFhAC&biw=1729&bih=876&dpr=2&mstk=AUtExfBeMvKZBMUrIoUhuOuTKLyzJ4cztWgRCD2UiC0UWGvx3dImTpJKGJOoXYUSz-77mXSlrpeDKf3yy2W03CH2nJ3NdGUB7SrnjDdDBo6mqUkY8WXvwRHTimwnm-NVoQXII23ZXjht9oVCeGrQ3GpHOX2PGzY5mM6QOb9IiT3gjAOJho5sTPVragyKUg6dpVzL6fpWxKfIeW4Fp3LfurHbPFaDSxDXijsalNhQ8mhA17z0cRCszsxhONZxjqafBUpOaU_fA2LRP8YELs6BVd7ko8-OeFKqSyvkT9pNkI-7UW7XAuLtzZSxRFQk-tsXdMzhoXHfRTajWbczGQ&csuir=1



def map_digits_alphabet(digit_string):
    try:
        num = int(digit_string)
        if 1 <= num <= 26:
            return chr(ord('A') + num - 1)
        else:
            return None
    except ValueError:
        return None

def num_decodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: empty string has one way to decode (no characters)
    dp[1] = 1  # Base case: first character can always be decoded if not '0'

    for i in range(2, n + 1):
        # Check for single digit decoding
        if 1 <= int(s[i-1:i]) <= 9:  # Current digit is '1' through '9'
            dp[i] += dp[i-1]

        # Check for two digit decoding
        if 10 <= int(s[i-2:i]) <= 26:  # Previous two digits form a number '10' through '26'
            dp[i] += dp[i-2]

    return dp[n]
def decode_and_count(number_string: str):
    if not number_string or not number_string.isdigit():
        print("Invalid input: Please provide a string containing only digits.")
        return [], 0
    example_decoding = []
    i = 0
    while i < len(number_string):
        # Try two-digit decoding first (if possible)
        if i + 1 < len(number_string):
            two_digit_num = number_string[i:i+2]
        if 10 <= int(two_digit_num) <= 26:
            example_decoding.append(map_digits_alphabet(two_digit_num))
            i += 2
            continue

        # Otherwise, try single-digit decoding
        single_digit_num = number_string[i:i+1]
        if 1 <= int(single_digit_num) <= 9:
            example_decoding.append(map_digits_alphabet(single_digit_num))
            i += 1
        else: # Invalid decoding (e.g., a '0' not preceded by '1' or '2')
            print("Invalid decoding encountered for example path.")
            example_decoding = [] # Clear the example as it's invalid
            break
    # Calculate total possible decodings using dynamic programming
    total_decodings = num_decodings(number_string)
    return example_decoding, total_decodings

# Example Usage:
number = "12"
example_decoding, count = decode_and_count(number)
print(f"Number: \"{number}\"")
print(f"Example decoding: {''.join(example_decoding) if example_decoding else 'None'}")
print(f"Total possible decodings: {count}\n") # Output: 2 (AB, L)
   