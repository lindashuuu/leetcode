class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            ##pivot
            if nums[mid]<nums[end]:
                if nums[mid]<target and target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
            
            else:
                if nums[start]<=target and target<nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            
                
        return -1
'''
https://www.cnblogs.com/grandyang/p/4325648.html
如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，则左半段是有序的，

'''
