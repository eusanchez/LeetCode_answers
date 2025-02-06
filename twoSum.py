#Two Sum Excercise. 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num is expected to be List[int]
        # -> List[int] this means that the function returns a list of integers.
        size = len(nums)
        for i in range(size-1):
            for j in range(i + 1, size):
                if nums[i] + nums[j] == target:
                    return [i,j]