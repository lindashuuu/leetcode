class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        fast=nums[0]
        slow=nums[0]
        
        while (nums[fast] and nums[nums[fast]]):
            
            slow=nums[slow]
            fast=nums[nums[fast]]
           
            if slow==fast:
                break
            
        
        fast=nums[0]
        while slow!=fast:
            fast=nums[fast]
            slow=nums[slow]
            
        return slow
'''
linkedlist cycle detection
because of pigenhole theory, there must be a duplicate

0 1 2 3 4
/  / / / 
1 2 3 4 x

0 1 2 3 4
/  / / / |
1 2 3 4 2 |    circle 
  |       |
  \ \ \ \ \



time:O(N)
spce: O(1)
'''
