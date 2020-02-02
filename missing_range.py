"""
Assumption: low != high
"""


def check_previous_val(ls, p_num, c_num, low):
    if p_num <= low:
        ls.append((compareToLow(p_num, low), c_num - 1))
    else:
        ls.append((p_num + 1, c_num - 1))


def compareToLow(num, low):
    if num == low:
        return low + 1
    elif num < low:
        return low


def compareToHigh(num, high):
    if num == high:
        return high - 1
    elif num > high:
        return high


def missing_ranges(nums, low, high):
    ls = []

    if len(nums) == 0:
        return ls.append((low, high))
    elif len(nums) == 1:
        if nums[0] <= low:
            low = compareToLow(nums[0], low)
            ls.append((low, high))
        elif nums[0] >= high:
            high = compareToHigh(nums[0], high)
            ls.append((low, high))
        else:
            ls.append((low, nums[0] - 1))
            ls.append((nums[0] + 1, high))
        return ls

    else:
        if nums[-1] <= low:
            low = compareToLow(nums[-1], low)
            ls.append((low, high))
            return ls

        if nums[0] >= high:
            high = compareToHigh(nums[0], high)
            ls.append((low, high))
            return ls

        diff = 0

        for i in range(len(nums)):
            if nums[i] < low:
                continue
            else:
                if nums[i] > high:
                    diff = high - nums[i - 1]
                    if diff > 1:
                        check_previous_val(ls, nums[i - 1], high + 1, low)
                    break
                else:
                    diff = nums[i] - nums[i - 1]
                    if diff > 1:
                        check_previous_val(ls, nums[i - 1], nums[i], low)

                    if nums[i] == high:
                        break

        if nums[-1] < high:
            ls.append((nums[-1] + 1, high))

    return ls


print(missing_ranges([1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)]
print(missing_ranges([1, 3, 5, 9], 1, 10))
print(missing_ranges([11, 13, 15, 110], 1, 10))
print(missing_ranges([-1, -3, -5, -10], 1, 10))
print(missing_ranges([1, 3, 15, 100], 1, 10))
print(missing_ranges([-1, 3, 15, 100], 1, 2))
print(missing_ranges([2], 1, 3))
