class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        count = 0
        res= sys.maxsize
        while right < len(nums):
            while right < len(nums) and count < s:
                count+=nums[right]
                right += 1
        
            while left < len(nums) and count >= s:
                res = min(res, right - left)
                count-=nums[left]
                left +=1        
        
        
        
        return res if res != sys.maxsize else 0

'''

minimum subarray length
https://www.cnblogs.com/grandyang/p/4501934.html
 for o(nlogn)
 

'''
