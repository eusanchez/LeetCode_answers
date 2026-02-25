class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char = []
        single = []

        for i in s:
            char.append(i)

        for x in char:
            if x not in single:
                single.append(x)
        
        print(single)

        return(len(single))