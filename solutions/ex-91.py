"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
    Input: [1,3,5,4,7]
    Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 

Example 2:
    Input: [2,2,2,2,2]
    Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxLength = 1
        n = len(nums)
        index = 0
        currentLength = 1

        if n == 0:
            return 0

        while index < n-1:
            if nums[index] < nums[index+1]:
                currentLength = currentLength + 1
                index = index + 1
            else:
                if currentLength > maxLength:
                    maxLength = currentLength
                currentLength = 1
                index = index + 1
        if currentLength > maxLength:
            maxLength = currentLength

        return maxLength