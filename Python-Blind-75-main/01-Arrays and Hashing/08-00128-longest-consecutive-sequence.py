# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# -------------------------------------------------------------------------------------------------------------------------------------------------

# HASHSET

# We can consider a number num as the start of a sequence if and only if num - 1 does not exist in the given array. 
# We iterate through the array and only start building the sequence if it is the start of a sequence. 
# This avoids repeated work. We can use a hash set for O(1) lookups by converting the array to a hash set.

# convert list to set for look up and remove duplicates
# iterate over the list- if n-1 is found, flow goes back to the for loop
# if n-1 is not found, it means n is the starting point of the sequence
# so initiate length = 1, and see if n + length is in the array
# if found, increment length
# keep incrementing length until the sequence is founf
# update the longest variable to get max length

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in seen:
                length = 1
                while (n + length) in seen:
                    length += 1
                longest = max(longest, length)
            
        return longest

Time Complexity = O(n)
Space Complexity = O(n)
