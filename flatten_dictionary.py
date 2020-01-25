intext = "{'a': 1,'b': {'c': 2, 'd': {'e': 3}}}"
l = []
flag = False
d = dict()

for i in intext:
    if i != ' ' and i != "'":
        if i == '{':
            flag = False
            continue

        if i == ':':
            flag = True
            continue

        if i == '}' or i == ',':
            flag = False
            l.pop()
            continue

        if flag:
            val = '.'.join(l)
            d[val] = int(i)
        else:
            l.append(i)

print(d)