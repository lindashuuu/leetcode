class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        pos pos 0 neg
        pos pos x neg neg
        
        """

        # 1  1  1
        # -1 -1 1 

        min1,min2 = sys.maxsize, sys.maxsize
        max1,max2,max3 = -sys.maxsize, -sys.maxsize, -sys.maxsize
        for num in nums:
            if num >= max1:
                max3 = max2  #order also matters!
                max2 = max1
                max1 = num
               
            elif num >= max2:
                max3 = max2
                max2 = num
                
            elif num >= max3:
                max3 = num
                
            if num <= min1:
                min2 = min1
                min1 = num
                
            elif num <= min2:
               
                min2 = num
                
        return max((min1*min2*max1), max1*max2*max3)
                
