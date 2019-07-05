class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return True
            ##pivot
            if nums[mid]<nums[end]:
                if nums[mid]<target and target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
            
            elif nums[mid]>nums[end]:
                if nums[start]<=target and target<nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                end-=1
            
                
        return False

'''

repeated numbers
[1,3,1,1,1]
[1,1,3,1]
mid is always on the left handside

[1,3,1,1,1]


'''
