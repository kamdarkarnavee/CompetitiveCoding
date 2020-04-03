def rotate(s, operations):
    ls = list(s)
    for element in operations:
        start_index, end_index, op = element.split(" ")
        start_index = int(start_index)
        end_index = int(end_index) + 1
        for index in range(start_index, end_index):
            val = ls[index]
            if op == 'L':
                new_val = chr((ord(val) - 1 - 97) % 26 + 97)
            else:
                new_val = chr((ord(val) + 1 - 97) % 26 + 97)
            ls[index] = new_val
    s = ''.join(ls)
    return s


s = 'abc'
operations = ["0 0 L", "2 2 L", "0 2 R"]
print(rotate(s, operations))

s = 'abc'
operations = ["0 1 L", "1 2 R", "0 2 R"]
print(rotate(s, operations))
