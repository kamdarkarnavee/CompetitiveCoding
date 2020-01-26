
def reverse_polish_notation(expr):
    ls = []
    for element in expr:
        if element in ['+', '-', '/', '*']:
           x = ls.pop()
           y = ls.pop()
           ls.append(eval(str(y) + element + str(x)))
        else:
            ls.append(element)
    return ls


# 1 - (2 + 3) * 2
print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
print(reverse_polish_notation([7, 8, '+', 3, 2, '+', '/']))
print(reverse_polish_notation([10, 3, 5, '*', 16, 4, '-', '/', '+']))
print(reverse_polish_notation([17, 10, '+', 3, '*', 9, '/']))
print(reverse_polish_notation([5, 4, 5, '*', '+', 5, '/']))