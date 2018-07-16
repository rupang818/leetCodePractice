class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        col = 0
        while col < n: 
            for row in reversed(range(n)): # 0, n
                matrix[col].append(matrix[row][0])    # Append new element
                matrix[row].pop(0)
            col+=1
