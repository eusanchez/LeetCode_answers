'''Works but is not efficient. Time limit exceeded.
class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        values = []
        n = len(nums)

        while len(values) != n:
            result = 0
            for i in range(n):
                result += i * nums[i]
            values.append(result) 
            
            last = nums[-1]
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = last

        
        return max(values)
'''