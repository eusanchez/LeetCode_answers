class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count = 0
        join = ""
        pairs = []
        len_word = len(word)

        # case where there is only one letter in the list
        if(len(sequence) == 1):
            for i in sequence:
                if (i == word):
                    return len(sequence)
                else:
                    return 0

        # case for a pair
        for s in range(len(sequence) - len_word + 1): 
            join = sequence[s:s+len_word]
            #print(join)
            pairs.append(join)
            #if (s < len(sequence)):
            #    join = sequence[s] + sequence[s+1]
            #    pairs.append(join)
            
        print(pairs)

        for pair in pairs:
            if(pair == word):
                count += 1
            
        return count
