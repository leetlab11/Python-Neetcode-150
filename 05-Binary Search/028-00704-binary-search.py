# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 
# Constraints:
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

# -------------------------------------------------------------------------------------------------------------------------------------------

# BINARY SEARCH
# start at 0th index and the last index of the list as l and r respectively.
# while the left boundary does not cross right boundary, start a loop
# if l = r,- this can be a case when there is only 1 element left to search; and this means that element is not looked into, so keep this in while condition
# calculate the midpoint- this can be done in 2 ways:
#  a. normal midpoint calculation- (l + r)//2
#  the above can lead to overflow- if r is close to 2^32 bit integer and if we add l to that, the addition will not happen
#  b. take the difference between the l and r and divide by 2- this is half the distance between l and r. Add this half distance to l- this will give halfway to r from l- ((r - l)/2) + l
# check if midpoint is > target-> this means we are looking for smaller value and r should be updated to shrink the window. We already have checked m, so r = m - 1
# check if midpoint is < target-> his means we are looking for greater value and l should be updated to shrink the window. We already have checked m, so l = m + 1
# if midpoint == target then return m
# if the entire list is iterated and target is not found, return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
        #   m = (l + r) // 2
            m = ((r - l)//2) + l

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1


Time Complexity = O(logn)
Space Complexity = O(1)
