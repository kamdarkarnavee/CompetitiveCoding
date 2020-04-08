def count_elements(arr):
    dictionary = dict()
    for i in arr:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    count = 0
    for i in dictionary:
        if i + 1 in dictionary:
            count += dictionary[i]
    return count


arr = [1, 2, 3]
print(count_elements(arr))
arr = [1, 1, 3, 3, 5, 5, 7, 7]
print(count_elements(arr))
