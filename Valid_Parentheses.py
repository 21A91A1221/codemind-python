def isValidParentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
t=int(input())
for i in range(t):
    s=input()
    if isValidParentheses(s):
        print(True)
    else:
        print(False)
