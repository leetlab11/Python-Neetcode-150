# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# checking length of the set of the list and length of the list itself. 
# Set will remove duplicates, so if duplicates are present, lengths will not be equal so return True. 
# If lengths are equal, no duplicates = False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        else:
            return False

# length of set is less than(or not equal to) length of list only when there are duplicates
# so if this is the case, return True else return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums):

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums):


Time Complexity = O(n)
Space Complexity = O(n)
          

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# create an empty set- seen
# iterate the list- if a number is already present in set, it means it's a duplicate, so return True
# if a number is not present in the set, add it to the set
# if ultimately True is not returned, return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

Time Complexity = O(n)
Space Complexity = O(n)

# Companies:
# Google- 6
# Amazon- 5
# Bloomberg- 4
# Microsoft- 3
# Meta- 2
# Yahoo- 3
# Oracle- 2
# Airbnb- 2
# Palantir Technologies- 2
# Paycom- 2
# Apple- 31
# Adobe- 21
# Uber- 18
# TCS- 7
# Yandex- 3
# JP Morgan- 2
# EPAM Systems- 2
# DE Shaw- 2
# Siemens- 2
# Accenture- 2
