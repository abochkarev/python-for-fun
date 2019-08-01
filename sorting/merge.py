def merge_sort(left, right):
    nums = left + right
    for i in range(1, len(nums)):
        cur_val = nums[i]
        while i > 0 and nums[i - 1] > cur_val:
            nums[i] = nums[i - 1]
            i -= 1
        nums[i] = cur_val
    return nums



def merge(nums):
    nums_len = len(nums)
    if nums_len <= 1:
        return nums
    else:
        div_nums_len = nums_len / 2
        left = merge(nums[:div_nums_len])
        right = merge(nums[div_nums_len:])
        return merge_sort(left, right)

print merge([3, 2, 5, 8, 1, 6, 9, 0, -1, 2])
