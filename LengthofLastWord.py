class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        list = s.split(" ")
        if '' in list:
            list = list.remove('')
        #list = [' '.join(string.split()) for string in list]
        print(list)
        #return len(list[-1])
        #print(list[-1])
