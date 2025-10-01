# Reverse bits of a given 32 bits signed integer.

# Example 1:

# Input: n = 43261596

# Output: 964176192

# Explanation:

# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000
# Example 2:

# Input: n = 2147483644

# Output: 1073741822

# Explanation:

# Integer	Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110
 
# Constraints:

# 0 <= n <= 231 - 2
# n is even.

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """

        binary_number = (((bin(n)[2:]).zfill(32))[::-1]) # converting int to binary
        #binary_32 = binary_number.zfill(32)
        #binary_reversed = (binary_number[::-1])
        n = (int(binary_number,2))
        return n
