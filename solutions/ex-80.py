"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
 

Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        if nums[0] >= 0 or nums[-1] <= 0:
            return nums[-1] * nums[-2] * nums[-3]

        if nums[-2] > 0:
            if nums[-3] > 0:
                r1 = nums[0] * nums[1] * nums[-1]
                r2 = nums[-1] * nums[-2] * nums[-3]
                if r1 > r2:
                    return r1
                else:
                    return r2
                    
        return nums[0] * nums[1] * nums[-1]