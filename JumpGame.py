class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        if not nums or len(nums)==1:
            return True
        dp=[False]*len(nums)
        for i in range(len(nums)):
            if i!=0 and not dp[i]:
                return False
            if i+nums[i]<len(nums) and dp[i+nums[i]]==True:
                pass
            
            else:
                
                start=i+nums[i]
               
                if i+nums[i]>=len(nums):
                    start=len(nums)-1
                for k in range(start,i,-1):
                    dp[k]=True
                
             
        return dp[-1]


'''
    
    
    O(N)
    
    greedy---------reach is the maximum distant
    
    class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        if not nums or len(nums)==1:
            return True
        reach,N=0,len(nums)
        
        for i in range(len(nums)):
            if reach>=len(nums)-1 or reach<i:
                break
            
            reach=max(reach,nums[i]+i)
        return reach>=len(nums)-1
        
    

'''
