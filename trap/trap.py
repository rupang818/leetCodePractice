class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max,right_max,answer,left,right = 0,0,0,0,len(height)-1
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left] 
                else: 
                    answer += left_max - height[left]
                left+=1
            else:
                if height[right] >= right_max:
                    right_max = height[right] 
                else:
                    answer += right_max - height[right]
                right-=1
        
        return answer
                
