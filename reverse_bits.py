def to_bits(n):
    return '{0:032b}'.format(n)


def reverse_num_bits(num):
    bits = to_bits(num)
    reverse = ''
    count = len(bits) - 1
    while count != -1:
        reverse += bits[count]
        count -= 1
    return int('0b' + reverse, 2)



print(to_bits(1234))
# 10011010010
print(reverse_num_bits(1234))
# 1260388352
print(to_bits(reverse_num_bits(1234)))
# 1001011001000000000000000000000
