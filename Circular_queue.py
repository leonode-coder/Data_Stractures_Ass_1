def is_palindrome(input_string):
    stack = []
    # Clean the string (remove spaces, lower case) for better accuracy
    clean_string = input_string.replace(" ", "").lower()

    # 1. Push all characters to stack
    for char in clean_string:
        stack.append(char)

    # 2. Pop and construct reversed string
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    # 3. Compare
    if clean_string == reversed_string:
        return True
    else:
        return False

# --- Testing the code ---
test_word = "Racecar"
if is_palindrome(test_word):
    print(f"'{test_word}' is a palindrome.")
else:
    print(f"'{test_word}' is NOT a palindrome.")
