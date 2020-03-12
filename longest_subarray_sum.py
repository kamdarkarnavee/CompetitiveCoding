def longest_subarray_sum(arr, target):
    i = 0
    j = 1
    ans_list = [-1]
    sum = arr[0]

    while j < len(arr):
        while sum <= target:
            if j < len(arr):
                sum += arr[j]
            else:
                break

            if sum == target:
                if len(ans_list) == 1 or ans_list[1] - ans_list[0] < j + 1 - i + 1:
                    ans_list = [i + 1, j + 1]
            j += 1
        sum -= arr[i]
        i += 1

    print(ans_list)


arr = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]
target = 15
longest_subarray_sum(arr, target)
