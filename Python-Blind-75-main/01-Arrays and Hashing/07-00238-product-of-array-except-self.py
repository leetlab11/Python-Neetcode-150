# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 
# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# -------------------------------------------------------------------------------------------------------------------------------------------------

# use a prefix arrays and a postfix arrays to store prefix values and postfix values respectively and multiply them to get the result
# pre values= product of values before that element
# post values = product of values after that element

# the result arrays have default values of 1 at each index
# default value of prefix and postifx variables is 1
# for pre values, the default value at 0th index is 1(prefix)
# for subsequent values, multiply prefix variable with nums[i] and assign those in the res array
# after this iteration is complete, start iteration in reverse to get post values
# for post values, default value at the last index is 1(postfix)
# for subsequent values, multiply postfix variable with nums[i] and multiply the result with already existing values in the res array
# return the res array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

Time Complexity = O(n)
Space Complexity = O(n) (res array; if o/p array is not considered extra space then O(1))

# Companies:
# Amazon- 10
# Google- 9
# Meta- 8
# Microsoft- 4
# Oracle- 2
# Infosys- 2
# Paypal- 2
# Asana- 2
# Apple- 6
# Bloomberg- 4
# Uber- 4
# IBM- 2
# LinkedIn- 2
# Flipkart- 2
# Sigmoid- 2
# Goldman Sachs- 2
# Autodesk- 2
# Accenture- 2
# Adobe- 18
# Intuit- 10
# Yahoo- 10
# Yandex- 7
# Tiktok- 6
# Warnermedia- 5
# Docusign- 4
# Zoho- 3
# Cisco- 3
# Walmart Labs- 2
