def move_zeros(nums):
    i = 0
    j = 0

    while j < len(nums):
        if nums[j] == 0 and nums[i] != 0:
            i = j

        if nums[j] != 0 and nums[i] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

        j += 1


# nums = [0, 0, 1]
# nums = [0, 1, 0, 3, 12]
nums = [1, 3, 0, 5]
move_zeros(nums)
print(nums)
