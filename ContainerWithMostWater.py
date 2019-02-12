class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        if not height:return 0
        res=0
        left,right=0,len(height)-1
       
        leftmax,rightmax=0,0 #index,weight
        while left<=right:
            
            res=max(res,(min(height[left],height[right])*(right-left)))
            if height[left]>height[right]:
                right-=1                
            else:

                left+=1
                
                
        
        
        
        return res



'''
O(n), O(1)


'''
