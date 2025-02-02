def is_palindrome(s: str) -> bool:
    stack = []
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Pop characters from the stack and compare with the original string
    for char in s:
        if char != stack.pop():
            return False
    
    return True

# Example usage
if __name__ == "__main__":
    test_string = "racecar"
    print(f"Is '{test_string}' a palindrome? {is_palindrome(test_string)}")
