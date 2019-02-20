class Solution:
    def maxNumber(self, nums1: 'List[int]', nums2: 'List[int]', k: 'int') -> 'List[int]':
        n,m=len(nums1),len(nums2)
        ret=[0]*k
        for i in range(k+1):
            j=k-i
            if i>n or j>m:continue
            
            num = self.mergeMax(self.maxSingleNumber(nums1,i), self.maxSingleNumber(nums2,j))
           
            ret = max(num, ret)
        return ret
    
    def mergeMax(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
                if nums1 > nums2:
                    ans += nums1[0],
                    nums1 = nums1[1:]
                else:
                    ans += nums2[0],
                    nums2 = nums2[1:]
        return ans
    
    def maxSingleNumber(self, nums, selects):
        ans = []
        size = len(nums)
        for x in range(size):
            while ans and len(ans) + size - x > selects and ans[-1] < nums[x]:
                    ans.pop()
            if len(ans) < selects:
                    ans += nums[x],
        return ans
'''
   O(k(M+N)^2)
   O(M+N)
    
'''
