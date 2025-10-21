
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = dict((i, nums.count(i)) for i in nums)
        lista = []
        for key , value in result.iteritems():
            if value >= k: 
                lista.append(key)
                print(lista)
            print(lista)
        print(lista)        
        return lista
