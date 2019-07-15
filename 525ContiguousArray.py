class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = -sys.maxsize
        count = 0
      
        history = {0:0}
        for i in range(len(nums)):
            count = count+1 if nums[i] else count-1
            
            if (count) in history:
                
                maxi = max(i+1-history[count], maxi)
            if count not in history:
                history[count] = i+1   
                    
        
        
        return maxi if maxi!= -sys.maxsize else 0
