# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SLIDING WINDOW:

# We can iterate through the given string with index r as the right boundary and l as the left boundary of the window. 
# We use a hash set to check if the character is present in the window or not. 
# When we encounter a character at index r that is already present in the window, we shrink the window by incrementing the l pointer until the window no longer contains any duplicates. 
# Also, we remove characters from the hash set that are excluded from the window as the l pointer moves. 
# At each iteration, we update the result with the length of the current window, r - l + 1, if this length is greater than the current result.

# maintain a substring between l and r pointers. Keep moving r to expand the substring, keep adding characters in the set
# as soon as a duplicate is found, shrink the window from left until all characters in the substring are unique, keep removing characters in set
# keep a variable to get the max length of the substring
# return that variable



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        res = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            res = max(res, (r - l) + 1)
        
        return res

Time Complexity = O(n) where n is length of the string
Space Complexity = O(m) where m is number of unique characters in the string

# Companies:
# Google- 33
# Amazon- 22
# Microsoft- 14
# Tiktok- 10
# Bloomberg- 9
# Meta- 8
# Turing- 4
# Goldman Sachs- 3
# IBM- 2
# Infosys- 2
# Oracle- 11
# Apple- 10
# Adobe- 4
# Zoho- 4
# Nvidia- 4
# Accenture- 4
# Yandex- 4
# EPAM Systems- 3
# Juspay- 3
# Tesla- 3
# Yahoo- 23
# Walmart Labs- 19
# Uber- 15
# Tinkoff- 14
# Spotify- 10
# Agoda- 8
# Flipkart- 7
# Bytedance- 7
# JP Morgan- 6
# eBay- 6
