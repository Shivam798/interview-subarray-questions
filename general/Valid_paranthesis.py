def valid_paranthesis(s):
    d={
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack=[]
    for char in s:
        if char in d:
            if  not stack or stack.pop()!=d[char]:
                return False
        else:
            stack.append(char)
    return len(stack)==0

print(valid_paranthesis("{[()]}"))