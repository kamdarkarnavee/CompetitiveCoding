
def prefixtopostfix(prefixes):
    ans = []
    for prestr in prefixes:
        postfix = []
        for i in range(len(prestr)-1, -1, -1):
            current = prestr[i]
            if current != '+' and current != '-' and current != '*' and current != '/':
                postfix.append(current)
            else:
                op1 = postfix.pop()
                op2 = postfix.pop()
                postfix.append(op1+op2+current)
        ans.extend(postfix)
    return ans


print(prefixtopostfix(['+23', '*4-34']))