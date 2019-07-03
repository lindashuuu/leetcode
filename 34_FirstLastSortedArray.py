class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        start,end=0,len(nums)-1
        while(start<=end):
            middle=(start+end)//2
            if nums[middle]>=target:
                end=middle - 1
            else:
                start=middle+1
      
        if start>=len(nums) or nums[start]!=target:
            return [-1,-1]
        result=[start,0]
        
        start,end=0,len(nums)-1
        while(start<=end):
            middle=(start+end)//2
         
            if nums[middle]<=target:
                start=middle+1
            else:
                end=middle - 1
                
        result[-1]=start-1
        return result
    
