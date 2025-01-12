# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1
 
# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# TWO POINTERS:

# use two pointers approach- l and r
# area =  length * height
# height- Container will be decided based on lower height; so move the lower height
# length- Length will be difference between the 2 pointers
# calculate the max area by multiplication and using max()
# loop will only run unless l < r
# return area

  
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0

        while l < r:
            area = max(area, (min(height[l], height[r]) * (r - l)))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return area

Time Complexity = O(n)
Space Complexity = O(1)

# Companies:
# Google- 15
# Amazon- 10
# Microsoft- 7
# Bloomberg- 7
# Snowflake- 2
# SAP- 2
# Meta- 5
# Goldman Sachs- 3
# Adobe- 2
# Apple- 2
# Wix- 2
# Tesla- 2
# Yahoo- 27
# Uber- 18
# Oracle- 15
# Flipkart- 11
# Yandex- 9
# Tiktok- 8
# Zoho- 7
# TCS- 4
# ByteDance- 4
# Walmart Labs- 3
