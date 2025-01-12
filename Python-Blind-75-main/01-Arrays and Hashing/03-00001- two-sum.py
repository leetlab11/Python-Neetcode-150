# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# -------------------------------------------------------------------------------------------------------------------------------------------------

# TWO PASS:

# create a hashmap where element is the key and it's index is value using enumerate(array)
# iterate over the enumerated array
# calculate the diff between n and target. That's the number we are looking for
# if that number is found in the hashmap and the index of that number is != i, that's what we are looking for
# return i and index of that number

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, n in enumerate(nums):
            seen[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen and seen[diff] != i:
                return [i, seen[diff]]

Time Complexity = O(n)
Space Complexity = O(n)

# -------------------------------------------------------------------------------------------------------------------------------------------------

# ONE PASS:

# here we'll add elements in the hashmap after checking if they already exists
# create an empty hashmap
# iterate over the array with index
# calculate diff- that's the number we are looking for
# check if the number is in the hashmap already
# if so, return the index of diff and current index
# if the diff is not in hashmap, add n to the hashmap
# this solution is guaranteed to get an answer; because when an element is checked for the first time; 
# it's diff value will not be in the hashmap. But when diff value is encountered, the first value will already be in the hashmap.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [i, seen[diff]]
            seen[n] = i

Time Complexity = O(n)
Space Complexity = O(n)

# Companies:
# Google- 214
# Amazon- 73
# Microsoft- 58
# Meta- 49
# Bloomberg- 31
# Apple- 9
# Oracle- 5
# Infosys- 4
# Walmart Labs- 4
# Visa- 5
# TCS- 11
# Yandex- 6
# IBM- 5
# Adobe- 5
# Tiktok- 5
# Accenture- 5
# Salesforce- 5
# SAP- 5
# Goldman Sachs- 4
# Uber- 4
# Yahoo- 90
# Capgemini- 12
# Zoho- 11
# Deloitte- 10
# Wipro- 10
# Spotify- 8
# Cisco- 7
# Nvidia- 7
# Tinkoff- 6
# Morgan Stanley- 6
