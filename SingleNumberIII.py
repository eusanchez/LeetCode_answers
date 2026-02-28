class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dictionary = {}
        single = []

        for number in nums:
            print(number)
            if number not in dictionary:
                dictionary[number] = 0
            dictionary[number] += 1

        for numbers in nums:
            if dictionary[numbers] == 1:
                single.append(numbers)

        return single