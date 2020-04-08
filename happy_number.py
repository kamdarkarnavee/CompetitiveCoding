
def happy_number(n):
    if n == 1:
        return True

    visited = set()
    visited.add(n)
    addition = 0

    while addition != 1:
        if addition in visited:
            return False

        visited.add(addition)
        addition = 0

        while n != 0:
            r = n % 10
            n = n // 10
            addition += r*r

        n = addition

    return True


print(happy_number(19))
print(happy_number(7))
print(happy_number(2))
