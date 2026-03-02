class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        numbers = []
        order = []
        second_largest = 0 
        for string in s:
            if string.isdigit():
                numbers.append(int(string))

        
        order = sorted(set(numbers))

        if len(order) <= 1:
            return -1
        else:
            second_largest = order[-2] 
            return second_largest
            


        