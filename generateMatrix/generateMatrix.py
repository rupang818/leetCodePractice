class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # array of n arrays (each array has n elements)
        i=1
        
        def generateMatrixFrom(n, startNum):
            # Algorithm:
            #   - fill the first row
            #   - fill the last column of each row
            #   - (reverse) fill the last row
            #   - (reverse) fill first column of each row
            #   - call self w/ reduced dim, n, and starting value (to fill), start
            matrix = [[-1 for _ in range(n)] for _ in range(n)]
            start_row,end_row,start_col,end_col=0,n,0,n
            numToInsert=startNum
            
            while numToInsert <= n*n:
                # first row
                for i in range(start_col,end_col):
                    matrix[start_row][i] = numToInsert
                    numToInsert+=1
                start_row+=1
                
                # fill last column of each row
                for y in range(start_row,end_row):
                    matrix[y][end_col-1] = numToInsert
                    numToInsert+=1
                end_col-=1
                
                # fill last row (reverse)
                for k in reversed(range(start_col,end_col)):
                    matrix[end_row-1][k] = numToInsert
                    numToInsert+=1
                end_row-=1
            
                # fill first column of each row
                for l in reversed(range(start_row,end_row)):
                    matrix[l][start_col] = numToInsert
                    numToInsert+=1
                start_col+=1
            return matrix
        
        return generateMatrixFrom(n, i)
