T = "2?:?8"

def Solution(T):
    ls = []
    i = 0
    x = T
    while True:
        if '?' in x:
            index = T.find('?', i)
            ls.append(index)
            i = index+1
            x = x[i:]

        else:
            break

    if len(ls) == 0:
        return T
    elif len(ls) == 4:
        return "23:59"
    else:
        if T[0] == '?' and T[1] == '?':
            T = T.replace('?', '2', 1)
            T = T.replace('?', '3', 1)
        else:
            if T[0] == '?' or T[1] == '?':
                if T[1] == '?':
                    if T[0] == '2':
                        T = T.replace('?', '3', 1)
                    else:
                        T = T.replace('?', '9', 1)
                else:
                    if T[1] > '3':
                        T = T.replace('?', '1', 1)
                    else:
                        T = T.replace('?', '2', 1)

    if T[3] == '?' and T[4] == '?':
        T = T.replace('?', '5', 1)
        T = T.replace('?', '9', 1)
    else:
        if T[3] == '?' or T[4] == '?':
            if T[4] == '?':
                T = T.replace('?', '9', 1)
            else:
                if T[3] == '?':
                    T = T.replace('?', '5', 1)

    return T


print(Solution(T))

