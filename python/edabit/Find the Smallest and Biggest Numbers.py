def min_max(nums):
	return [min(nums), max(nums)]

#or

def min_max(nums):
  return [sorted(nums)[0], sorted(nums)[-1]]

#or

def min_max(nums):
    nums.sort()
    return [nums[0],nums[-1]]