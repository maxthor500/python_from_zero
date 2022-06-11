
def minOperations(nums, x):
    if not len(nums) or not x:
        return

    total = sum(nums)
    remainder = total - x
    largest_subarray_len = -1
    current_sum = 0

    count = 0
    for index in range(len(nums)):
        current_sum += nums[index]
        while current_sum > remainder and count <= index:
            current_sum -= nums[count]
            count += 1
        if current_sum == remainder:
            largest_subarray_len = max(
                largest_subarray_len, index - count + 1)

    if largest_subarray_len == -1:
        return largest_subarray_len

    return len(nums) - largest_subarray_len


nums2 = [5, 6, 7, 8, 9]
x2 = 4

nums1 = [1, 1, 4, 2, 3]
x1 = 5

nums3 = [3, 2, 20, 1, 1, 3]
x3 = 10


print(minOperations(nums1, x1))
print(minOperations(nums2, x2))
print(minOperations(nums3, x3))
