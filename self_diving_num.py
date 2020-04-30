def selfDividingNumbers(left, right):
    ans = []
    for i in range(left, right + 1):
        current = i
        flag = True
        while i:
            r = i % 10
            i = i // 10
            if r == 0 or current % r != 0:
                flag = False
                continue
        if flag:
            ans.append(current)
    return ans


print(selfDividingNumbers(1, 22))
