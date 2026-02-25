class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        #column = len(matrix[0])
        #row = len(matrix)
        #result = []

        #col = [matrix[i][1] for i in range(len(matrix))]

        '''for j in range(column):
            col = []
            for i in range(row):
                col.append(matrix[i][j])
            result.append(col[::-1])'''

        n = len(matrix)

        # Step 1: Transpose (swap rows and columns)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)

        # Step 2: Reverse each row
        for i in range(n):
            #matrix[i] = complete row
            #matrix[i][::-1] = complete row flipper over. 
            matrix[i] = matrix[i][::-1]
