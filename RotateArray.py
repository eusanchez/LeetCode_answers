class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) == 1):
            return nums

        saved = 0
        if(len(nums) % 2 == 0):
            for i in range(0, k):
                nums[i], nums[i+k] = nums[i+k], nums[i]
        else:
            for i in range(0, k):
                nums[i], nums[i+k+1] = nums[i+k+1], nums[i]
            saved = nums[k]
            nums.remove(nums[k])
            nums.append(saved)
            