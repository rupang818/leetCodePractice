class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pt2=len(height)-1
        maxArea=0
        i=0
        while i < len(height):
            w=pt2-i
            if w == 0:
                break
            h=min(height[i],height[pt2])
            newMax=w*h
            maxArea=max(maxArea,newMax)
            if h==height[pt2]:    # back is min
                pt2-=1
            else:
                i+=1
            
        return maxArea

