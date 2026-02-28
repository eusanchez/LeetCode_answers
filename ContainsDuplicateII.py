class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        dictionary = {}
        for position, number in enumerate(nums):
            if number in dictionary and position - dictionary[number] <= k:
                return True
            dictionary[number] = position

        return False

        