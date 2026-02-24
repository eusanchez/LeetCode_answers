class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        column = len(matrix[0])
        row = len(matrix)
        result = []

        #col = [matrix[i][1] for i in range(len(matrix))]

        '''for j in range(column):
            col = []
            for i in range(row):
                col.append(matrix[i][j])
            result.append(col[::-1])'''

  
        
        
