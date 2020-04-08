import math


def max_subarray(nums):
    max = -math.inf
    summation = 0

    for i in range(len(nums)):
        summation += nums[i]
        if nums[i] > summation:
            summation = nums[i]
        if summation > max:
            max = summation

    return max


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(nums))
nums = [-2, 1]
print(max_subarray(nums))
nums = [1]
print(max_subarray(nums))
nums = [1, 2]
print(max_subarray(nums))
