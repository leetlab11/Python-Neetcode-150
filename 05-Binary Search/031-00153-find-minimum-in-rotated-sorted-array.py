# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

# Constraints:
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

# --------------------------------------------------------------------------------------------------------------------------------------

# array is rotated but still sorted, so we can use the sorted property.
# there are 2 sorted arrays- left and right
# find m by taking the midpoint of l and m(floor division)
# when we are in left array, try to search right as that might have smaller elements;
# so when m >= l that means we are in left array; so l = m+1(we are trying to move right)
# when we are in right array, try to search left as the left side in right array will have smaller elements
# so when m < l that means we are in right array; so r = m-1(we are trying to move left)
# when we are in an array that is sorted, this algorithm won't work, so search for the leftmost element and compare with res
# if that l is smaller than res, that is the o/p and the loop will break

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else: 
                r = m - 1
        
        return res

Time Complexity = O(logn)
Space Complexity = O(1)


# Companies:
# Meta- 4
# Tiktok- 4
# Google- 3
# Apple- 2
# Microsoft- 7
# Amazon- 6
# Goldman Sachs- 3
# Adobe- 7
# Bloomberg- 6
# Yahoo- 4
# Yandex- 3
# Paypal- 3
# eBay- 3
# ServiceNow- 3
# ByteDance- 2
# Tesla- 2
# Uber- 2


