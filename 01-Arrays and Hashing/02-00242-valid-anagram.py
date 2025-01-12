# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SORTING
# compare the sorted strings 
# if the sorted strings are equal, they are anagrams, so return True, else return False
# it is optional to check for lengths

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#        if len(s) != len(t):
#            return False

        return sorted(s) == sorted(t)
      
Time Complexity = O(nlogn + mlogm) where n is length of s and m is length of t
Space Complexity = O(n + m) or O(1) depending on the sorting algorithm- (ChatGPT says O(n + m))

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# HASH TABLES: Maintain a frequency table of each letter in the strings
# first compare length of strings; if they are equal then go ahead
# create 2 empty hash tables; 1 for each string
# iterate through the length of the string(any string, because both lengths are same)
# when the loop is on a character, add 1 to the count. But what if that character is met for the first time? 
# use hashtable.get() method, where 1st parameter is the character(s[i]), 2nd is the default value(0). 
# 0 because we are adding 1 to it when it's encountered.
# compare both the hashtables. If they are not equal, they are not anagrams, so return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(0, len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

# To compare both the hash tables, start a loop.  
# If the value(freq) of a key(character) in hash table S is not equal to that in T, return False.
# But what if that character is not in T at all? The comparison will throw error. So set a default value of that character to 0.
# If the loop ends without returning false, that means they are anagrams, so return True

        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False
        
        # return True
          
        return countS == countT

Time Complexity = O(n + m)
Space Complexity = O(1) since we have at most 26 different characters

# Companies:
# Bloomberg- 15
# Google- 11
# Amazon- 8
# Microsoft- 5
# Meta- 3
# Apple- 3
# Affirm- 3
# Uber- 3
# EPAM Systems- 2
# Yelp- 2
# Adobe- 12
# Yahoo- 9
# TCS- 5
# Accenture- 5
# Oracle- 3
# Goldman Sachs- 3
# JP Morgan- 2 
# Walmart Labs- 2
# Tiktok- 2
