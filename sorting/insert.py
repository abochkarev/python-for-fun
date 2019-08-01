def insert(nums):
    for idx in range(1, len(nums)):
        cur_val = nums[idx]
        while idx > 0 and nums[idx - 1] > cur_val:
            nums[idx] = nums[idx - 1]
            idx = idx - 1
        nums[idx] = cur_val
    return nums

print insert([3, 2, 3, 5, 6, 1, 5, 7, 12, 5])
