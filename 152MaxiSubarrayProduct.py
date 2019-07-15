class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        2 -2 2 3
        2   2 3   
        """
        res, maxi, mini = nums[0],nums[0],nums[0]
        
        for i in range(1,len(nums)):
            
            if nums[i]<0:
                maxi, mini = mini, maxi
            maxi = max(nums[i], maxi*nums[i])
            mini = min(nums[i], mini*nums[i])
          
            res = max(maxi, res)
            
        return res
