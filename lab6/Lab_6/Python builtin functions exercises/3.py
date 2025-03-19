def is_palindrome(s):
    result = s == s[::-1]
    print(f"String: {s} is palindrome: {result}")
    return result

is_palindrome("madam")