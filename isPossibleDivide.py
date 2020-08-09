def update_count(start, sorted_table, hash_table):
    if hash_table[start] == 1:
        del hash_table[start]
        sorted_table.remove(start)
    else:
        hash_table[start] -= 1


def isPossibleDivide(nums, k):
    num_len = len(nums)
    if k == 1:
        return True

    if num_len % k != 0:
        return False

    total_sub_arr = num_len // k

    hash_table = dict()
    for i in nums:
        if i in hash_table:
            hash_table[i] += 1
        else:
            hash_table[i] = 1

    sorted_table = sorted(hash_table.keys())

    for i in range(total_sub_arr):
        start = sorted_table[0]
        update_count(start, sorted_table, hash_table)
        for j in range(k-1):
            if start+1 in hash_table:
                update_count(start+1, sorted_table, hash_table)
                start += 1
            else:
                return False
    return True


nums = [3, 3, 2, 2, 1, 1]
k = 3
print('Divide nums:', nums, 'in subarray of k:', k, 'consecutive integers')
print('Answer: Is Possible to divide -> ', isPossibleDivide(nums, k))

