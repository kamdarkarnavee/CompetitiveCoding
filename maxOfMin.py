arr = [1, 5, 7, 8, 9, 2, 4, 3]
window_size = 5


def maxOfMin(arr, window_size):
    arr_length = len(arr)
    if arr_length < window_size or arr_length == 1:
        return min(arr)

    maxofmin = float('-inf')
    for i in range(arr_length - window_size):
        minimum = min(arr[i:i+window_size])

        if minimum > maxofmin:
            maxofmin = minimum

    return maxofmin


print(maxOfMin(arr, window_size))