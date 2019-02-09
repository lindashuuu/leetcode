class Solution:
    def containsNearbyAlmostDuplicate(self, nums: 'List[int]', k: 'int', t: 'int') -> 'bool':
      
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in range(n):
           
            m = nums[i] // w if w!=0 else nums[i]
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] // w if w!=0 else nums[i-k]]
            
        return False

'''
             1.   use // because / can have 0.5
             2.   be aware of w=0 (division by zero error)
             
             for   d[m] = nums[i], we can be sure the distance is always t
             in two near bucket and just keep one element
             
             because
             0--t t+1--2t+1   2t+2...

             a  b        a
             2  1        3

            if a apear after b , a and b would return true

'''
