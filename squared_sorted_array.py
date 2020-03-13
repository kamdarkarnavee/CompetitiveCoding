def squared_sorted_array(arr):
    arr_length = len(arr)
    output_arr = [0] * arr_length

    i = 0
    j = arr_length - 1
    k = arr_length - 1

    while i <= j:
        if arr[i] < 0:
            # Only taking absolute value of first element as the array is always sorted
            if abs(arr[i]) > arr[j]:
                output_arr[k] = arr[i] ** 2
                i += 1
            else:
                output_arr[k] = arr[j] ** 2
                j -= 1
        else:
            output_arr[k] = arr[j] ** 2
            j -= 1
            i += 1
        k -= 1

    print(output_arr)


# arr = [-3, -2, -1, 4]
arr = [-3, -2, -1, 0, 1, 2, 3, 4]

squared_sorted_array(arr)
