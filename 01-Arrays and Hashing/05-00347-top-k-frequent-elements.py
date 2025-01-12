# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
 
# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# -------------------------------------------------------------------------------------------------------------------------------------------------

# HASHMAP

# create a hashmap where num is key and it's freq is the value
# create a bucket list where index is freq and value at each index is a list of nums that has that freq
# we are creating a bucket of frequencies because at max, all the elments in the nums list will be same, and will be in the last bucket
# eg if there are nine 7's in the nums list and length of nums list = 9, so freq bucket list will from 0th index to 9th index = length 10
# bucket list will be length of nums + 1, because there's a 0th index
# create an o/p list res that is empty
# iterate a loop on the bucket list in reverse order till 1st index(because 0th index will be empty)
# because we want top frequent elements, so the later in list the higher the freq highest
# iterate loop in the inner list(each bucket)
# append in the res list
# when length of res == k, return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numToFreq = {}
        freqBuckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            numToFreq[n] = 1 + numToFreq.get(n, 0)
        
        for num, count in numToFreq.items():
            freqBuckets[count].append(num)

        
        res = []
        for i in range(len(freqBuckets) - 1, 0, -1):
            for j in freqBuckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
                  

Time complexity = O(n)
Space complexity = O(n)
