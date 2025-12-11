#Two Sum Excercise. 

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num is expected to be List[int]
        # -> List[int] this means that the function returns a list of integers.
        size = len(nums)
        for i in range(size-1):
            for j in range(i + 1, size):
                if nums[i] + nums[j] == target:
                    return [i,j]
                

---- SECOND ATTEMPT -----

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # lista = nums[:] #copy of a list or with lista=nums.copy()
        # counter = 0 
        # for element1 in nums:
        #     nums.remove(element1)
        #     counter += 1
        #     for element2 in nums:
        #         if (element1 + element2) == target:
        #             print(element1, element2)
        #             return [lista.index(element1), nums.index(element2)+counter]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
