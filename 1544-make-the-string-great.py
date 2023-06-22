def makeGood(string):
    stack = []
    for char in list(string):
        if stack and abs(ord(char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


print(makeGood("leEeetcode"))
print(makeGood("abBAcC"))
print(makeGood("s"))
