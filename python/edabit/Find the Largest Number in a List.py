def findLargestNum(nums):
	return max(nums)

#or

def findLargestNum(nums):
    nums.sort()
    return nums[-1]

#or

def findLargestNum(nums):
	return sorted(nums)[-1]

#or

def findLargestNum(nums):
  largest = nums[0]
  for i in nums:
    if i > largest:
      largest = i
  return largest