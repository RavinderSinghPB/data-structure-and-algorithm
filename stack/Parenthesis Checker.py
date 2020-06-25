def ParenthesisChecker(exp):

    stack = []
    ans = "balanced"
    dic = {'(' : ')', '{' : '}', '[' : ']'}
    for i in exp:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif not stack or dic[stack.pop()] != i:
            ans = "not balanced"
            break
    if stack:
        ans = "not balanced"
    return ans


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        exp = input()
        print(ParenthesisChecker(exp))

