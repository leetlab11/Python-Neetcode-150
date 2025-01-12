# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# -------------------------------------------------------------------------------------------------------------------------------------------------

# STACK:

# We can use a stack to store characters. Iterate through the string. For an opening bracket, push it onto the stack. 
# If the bracket is a closing type, check for the corresponding opening bracket at the top of the stack. 
# If we don't find the corresponding opening bracket, immediately return false. 
# This works because in a valid parenthesis expression, every opening bracket must have a corresponding closing bracket. 
# The stack is used to process the valid string, and it should be empty after the entire process. 
# This ensures that there is a valid substring between each opening and closing bracket.

# create an empty list(stack)
# create a hashmap manually; where close brackets are keys and open are values
# iterate through the string
# if we encounter a closed bracket, check if the stack9(stack) is not null and the top element of the stack(stack[-1]) is equal to the value of the key we just encountered(opening bracket of the closing bracket we just encountered)
# if so, pop the bracket from the stack
# if we encounter an open bracket, add it to the stack(append)
# if stack is empty at the end, it means all brackets matched, so parenthesis are valied- return True
# if stack is not empty, return False


class Solution:
    def isValid(self, s: str) -> bool:

        closeToOpen = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

Time Complexity = O(n)
Space Complexity = O(n)

# Companies:
# Amazon- 18
# Google- 17
# Bloomberg- 14
# Meta- 13
# Microsoft- 7
# LLinkedIn- 7
# Apple- 6
# Intuit- 4
# Turing- 4
# IBM- 3
# Tiktok- 5
# TCS- 4
# Zoho- 4
# Tripadvisor- 4
# Walmart Labs- 3
# eBay- 3
# Blackrock- 3
# Infosys- 2
# Oracle- 2
# Epic Systems- 2
# Yandex- 36
# Adobe- 34
# Uber- 27
# Yahoo- 20
# JP Morgan- 18
# ServiceNow- 12
# Ozon- 10
# Accenture- 9
# EPAM Systems- 8
# Goldman Sachs- 8
