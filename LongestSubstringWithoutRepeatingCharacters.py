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
    
'''class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char = []
        single = []
        start = 0 
        max_lenght = 0
        window = []

        for i in s:
            char.append(i)

        duplicates = set(char)
        for i in s:
            if i not in window:
                window.append(i)
                if(len(window) == len(char)):
                    return len(window)
            else:
                window = []

        '''