
def search(nums, target):
    def find_element(nums, target):
        lo = 0
        hi = len(nums)-1

        while (lo<=hi):
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[lo]:
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if target <= nums[hi] and target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
    return find_element(nums, target)

nums = [4,5,6,7,0,1,2]
target = 0

print(search(nums, target))