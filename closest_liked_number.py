def is_ascending(ls):
    for i in range(len(ls) - 1):
        if int(ls[i]) >= int(ls[i + 1]):
            return False
    return True


def is_liked(ls, n):
    current_num = int(''.join(ls))
    return is_ascending(ls) and current_num < n


def check_for_zero(ls, pos, max_val):
    if ls[pos] != '0':
        ls[pos] = str(int(ls[pos]) - 1)
    else:
        ls[pos] = str(max_val)
        pos -= 1
        max_val -= 1


def closest_liked_number(n):
    if len(str(n)) == 1:
        return n

    ls = list(str(n))
    flag = is_ascending(ls)
    max_val = 9
    pos = len(ls) - 1
    if flag:
        return n

    ls[pos] = str(max_val)
    pos -= 1
    max_val -= 1
    check_for_zero(ls, pos, max_val)
    while not flag:
        liked = is_liked(ls, n)
        if liked:
            return int(''.join(ls))
        else:
            if pos > -1:
                ls[pos] = str(max_val)
                max_val -= 1
                pos -= 1
                if pos > -1:
                    check_for_zero(ls, pos, max_val)
            else:
                return -1


if __name__ == '__main__':
    print(closest_liked_number(1234))  # output: 1234
    print(closest_liked_number(2543))  # output: 2489
    print(closest_liked_number(998))  # output: 789
    print(closest_liked_number(100000))  # output: 56789
    print(closest_liked_number(887))  # output: 789
