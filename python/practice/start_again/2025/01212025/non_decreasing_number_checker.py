#   https://www.geeksforgeeks.org/problems/difficult-problems1303/1?page=1&category=Pattern%20Searching&sortBy=submissions
#   https://search.brave.com/search?q=Given+a+Number+N+in+String+form%2C+Print+1+If+the+digits+of+the+number+are+in+non-decreasing+or+non-increasing+order%2C+else+print+0.&source=web&summary=1&conversation=822d8552afeacf7086ab1d


def is_tidy_or_antitidy(number_str):
    # Convert the string to a list of digits
    digits = [int(digit) for digit in number_str]
    
    # Check if digits are in non-decreasing order
    is_non_decreasing = all(digits[i] <= digits[i+1] for i in range(len(digits)-1))
    
    # Check if digits are in non-increasing order
    is_non_increasing = all(digits[i] >= digits[i+1] for i in range(len(digits)-1))
    
    # If either condition is true, return 1, else return 0
    return 1 if is_non_decreasing or is_non_increasing else 0

if __name__ == "__main__":
    number_str = "1233"
    number_str2 = "1263"
    print (is_tidy_or_antitidy(number_str))
    print (is_tidy_or_antitidy(number_str2))