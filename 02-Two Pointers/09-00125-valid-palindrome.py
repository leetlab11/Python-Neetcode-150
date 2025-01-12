# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
  
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
  
# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 
# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATING A NEW STRING:

# create a new empty string
# iterate over the current string- if a character is alphanumeric, lowercase it and it to the new string.
# compare new string and new string in reverse; return answer

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newStr = ''

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]

Time Complexity = O(n)
Space Complexity = O(n)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# TWO POINTERS:

# define a function to check if a character is alphanumeric using ord(c)
# use two pointers approach- l and r
# keep a check for l < r
# keep check again for l < r to ensure the pointers stay within bounds during the search for alphanumeric characters. 
# this helps ensure that once the pointers meet or cross, the function can return without unnecessary checks.
# if an alphanumeric character is not met, go ahead(l + 1, r -1  )
# if an alphanumeric character is met, lowercase and compare l and r
# if they are not equal, return False
# if they are equal, loop continues
# if loop does not return False and exits, return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
      
#       can use Python in-built function isalnum()
#       return c.isalnum()

Time Complexity = O(n)
Space Complexity = O(1)

# Companies:
# Meta- 53
# Google- 5
# Amazon- 4
# Apple- 2
# Oracle- 2
# Microsoft- 8
# Bloomberg- 4
# Uber- 3
# TCS- 2
# Goldman Sachs- 2
# Zenefits- 2
# Yandex- 45
# Adobe- 20
# Yahoo- 6
# Toast- 6 
# EPAM Systems- 5
# Spotify- 4
# Tiktok- 3
# American Express- 3
# Accenture- 3
# Deloitte- 2
