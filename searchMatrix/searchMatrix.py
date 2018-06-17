class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 1. select the array (index) that contains value bigger than target (call it "i")
        # 2. start searching for the array[i-1]
        # 3. Since arrays are sorted, try using binary search
        #      - check mid element  => if matches, return true
        #                           => if array[i-1][mid] < target, search array[i-1][mid+1:]
        #                           => if array[i-1][mid] > target, search array[i-1][:mid-1]
        if not matrix:
            return False
        elif not matrix[0]:
            print("HERE?")
            return False
        
        def binarySearchArr(arr, target):
            if not arr:
                return False
                
            mid_index=int(len(arr)/2)
            if arr[mid_index] == target:
                return True
            elif arr[mid_index] < target:
                return binarySearchArr(arr[mid_index+1:],target)
            else:
                return binarySearchArr(arr[:mid_index],target)
        
        i=0
        while i < len(matrix):
            if target < matrix[i][0]:
                break
            elif target == matrix[i][0]:
                return True
            i+=1
        return binarySearchArr(matrix[i-1],target) if i > 0 else False
