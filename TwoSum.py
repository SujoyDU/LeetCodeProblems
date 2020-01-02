"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

#Here the idea is to create a dictionary of items with their index numbers from the list
# whose values does not compute the target. 
# when target -val aka the complement  is found in the list then thats the desired index

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        itemDict = {}
        for idx, val in enumerate(nums):
            if (target - val) not in itemDict:
                itemDict[val] = idx
            else: return [itemDict[target-val],idx]


solve = Solution()
nums: List[int]
target:int
nums= [2,7,11,15]
target = 9
print(solve.twoSum(nums,target))