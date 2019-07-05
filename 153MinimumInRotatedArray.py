class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini=sys.maxsize
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if (nums[mid]<nums[right]):
                mini=min(nums[mid],mini)
                right=mid-1
            else:
                mini=min(nums[left],mini)
                left=mid+1
        
        
        
        
        return mini
