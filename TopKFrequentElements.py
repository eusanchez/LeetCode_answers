
#class Solution(object):
    #def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #result = dict((i, nums.count(i)) for i in nums)
        #lista = []
        #for key , value in result.iteritems():
            #if value >= k: 
                #lista.append(key)
                #print(lista)
            #print(lista)
        #print(lista)        
        #return lista

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = [[] for i in range(len(nums) +1)]
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)


        answer = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer
