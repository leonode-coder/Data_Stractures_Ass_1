def is_palindrome(text):
    stack = []
    clean_text = "".join(char.lower() for char in text if char.isalnum())

    for char in clean_text:
        stack.append(char)

    reversed_text = ""
    while stack:
        reversed_text += stack.pop()

    if clean_text == reversed_text:
        return True
    else:
        return False

if __name__ == "__main__":
    word = "Racecar"
    result = is_palindrome(word)
    
    if result:
        print(f"'{word}' is a Palindrome ")
    else:
        print(f"'{word}' is NOT a Palindrome ")
