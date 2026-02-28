class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dictionary = {}

        for number in nums:
            if number not in dictionary:
                dictionary[number] = 0
            dictionary[number] += 1

        for number in nums:
            if dictionary[number] == 1:
                return number

#we can also use dictionaries not just for number/position but also for number/occurence.


'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in nums:
            if nums.count(x) == 1:
                return x
'''