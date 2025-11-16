"""
Valid Parentheses Problem Implementation in Python

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Time Complexity: O(n)
"""

def is_valid(s):
    """
    Check if the string has valid parentheses.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            # Closing bracket
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            # Opening bracket
            stack.append(char)

    return not stack

# Example usage and test cases
if __name__ == "__main__":
    test_cases = [
        "()",           # True
        "()[]{}",       # True
        "(]",           # False
        "([)]",         # False
        "{[]}",         # True
        "",             # True
        "[",            # False
        "((",           # False
        "))",           # False
    ]

    for s in test_cases:
        print(f"'{s}' is valid: {is_valid(s)}")
