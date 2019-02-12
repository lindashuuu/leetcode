class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        if not height: return 0
        dp_left=[0]*len(height)
        dp_right=[0]*len(height)
        dp_left[0]=height[0]
        dp_right[-1]=height[-1]
        
        left_max=height[0]
        for i in range(1,len(height)):
            if height[i]>left_max:
                left_max=height[i]
            dp_left[i]=left_max
        
        right_max=height[-1]
        for i in range(len(height)-1,-1,-1):
            
            if height[i]>right_max:
                right_max=height[i]
            dp_right[i]=right_max
        result=0
        for i in range(len(height)):
            result+=(min(dp_right[i],dp_left[i])-height[i])
        return result
'''
    improve: use one dp array (store min(left,right))
     for i in range(1,len(height)):
            if height[i]>left_max:
                left_max=height[i]
            dp_left[i]=left_max
        
        right_max=height[-1]
        for i in range(len(height)-1,-1,-1):
            
            if height[i]>right_max:
                right_max=height[i]
            dp_left[i]=min(dp_left[i],right_max)


    improve: use two pointers (similar to container water)
    class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        if not height: return 0
        result=0
        rightmax,leftmax=0,0
        left,right=0,len(height)-1
        
        while left<=right:
            if height[left]<height[right]:
                if height[left]>leftmax:
                    leftmax=height[left]
                result+=leftmax-height[left]
                left+=1
                
            else:
                
                if height[right]>rightmax:
                    rightmax=height[right]
                result+=rightmax-height[right]
                right-=1
        return result
'''
