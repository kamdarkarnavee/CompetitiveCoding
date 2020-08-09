def findLeastNumOfUniqueInts(arr, k):
    len_arr = len(arr)
    if k == len_arr:
        return 0

    hash_table = dict()
    for i in arr:
        if i in hash_table:
            hash_table[i] += 1
        else:
            hash_table[i] = 1

    sorted_table = sorted(hash_table.items(), key=lambda x: x[1])
    count = 0
    for i in range(len(sorted_table)):
        count += sorted_table[i][1]
        if count == k:
            return len(sorted_table[i+1:])
        elif count > k:
            return len(sorted_table[i:])


arr = [4, 3, 1, 1, 3, 3, 2]
k = 3
print('Least Num Of Unique Ints:', findLeastNumOfUniqueInts(arr, k))
