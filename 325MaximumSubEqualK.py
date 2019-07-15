class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        
        pos pos 0 neg neg
        """
        maxi = -sys.maxsize
        count = 0
      
        history = {0:0}
        for i in range(len(nums)):
            count+=nums[i]
            if count not in history:
                history[count] = i+1
            if (count-k) in history:
                
                maxi = max(i+1-history[count-k], maxi)
               
                    
        
        
        return maxi if maxi!= -sys.maxsize else 0
'''
x-(past) = k
x-k = past

'''
