class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        list = s.split()
        
        if not list:
            return 0

        return len(list[-1])
