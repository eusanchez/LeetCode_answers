class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(e for e in s if e.isalnum()).lower()
        if s == s[::-1]:
            return True
        else:
            return False 


------ NEW CODE ------ 

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]
        
        #lista_reversed = lista[::-1]
        #return lista_reversed == lista
