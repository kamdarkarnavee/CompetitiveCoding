ls = ['1', '+', '-2', '+', '3']
print(ls.index('+'))


def operation(ls, m):
    x = 0
    if ls[m] == '+':
        x = int(ls[m - 1]) + int(ls[m + 1])
    if ls[m] == '-':
        x = int(ls[m - 1]) - int(ls[m + 1])
    if ls[m] == '*':
        x = int(ls[m - 1]) * int(ls[m + 1])
    if ls[m] == '/':
        x = int(ls[m - 1]) / int(ls[m + 1])
    print(ls)
    ls.pop(m - 1)
    ls.pop(m - 1)
    ls.pop(m - 1)
    ls.insert(m-1, x)


operators = ['+', '-', '*', '/']
while True:
    if '*' in ls or '/' in ls or '+' in ls or '-' in ls:

        while '*' in ls or '/' in ls:
            m = n = 999
            if '*' in ls:
                m = ls.index('*')
            if '/' in ls:
                n = ls.index('/')
            operation(ls, min(m, n))
        while '+' in ls or '-' in ls:
            m = n = 999
            if '+' in ls:
                m = ls.index('+')

            if '-' in ls:
                n = ls.index('-')

            operation(ls, min(m, n))
    else:
        print(ls[0])
        break

