class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        if len(nums)==1 and abs(nums[0]-24)<0.001:
            
            return True
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    nums_except_current=[nums[k] for k in range(len(nums)) if (k!=i and k!=j)]
                    possible_outcomes={nums[i]+nums[j],nums[i]*nums[j],nums[i]-nums[j],nums[j]-nums[i]}
                    if nums[i]>0:possible_outcomes.add(nums[j]/nums[i])
                    if nums[j]>0:possible_outcomes.add(nums[i]/nums[j])
                    for num in possible_outcomes:
                        nums_except_current.append(num)
                        if self.judgePoint24(nums_except_current): return True
                        nums_except_current.pop()
                        
        return False
'''
To start, we have a total of 4 numbers, 3 operators to fill.
[num] op [num] op [num] op [num]
Operators can be repeatedly used, but numbers can not.

So we have 4x3x2x1 numbers and 4x4x4 operators to choose from

There are 6 ways to place ()

( [num] op [num] ) op  [num]  op  [num]
[num] op ( [num] op  [num] )  op  [num]
[num] op [num] op  ( [num]  op  [num] )

( [num] op [num] ) op  ( [num]  op  [num] )

( [num] op [num] op  [num] ) op  [num]
[num] op ( [num] op  [num]  op  [num] )

Each of these combination has a chance (and more) to contribute to ( [num] op [num] op [num]  op  [num] ) so we don't need to count this as the 7th way.

Hence the total number possibilities is 4x4x4x4x3x2x6 = 9216 with some overhead.

so O(1) time and O(1) space

solution:
that gives us an upper bound of 12 * 6 * 2 * 4 * 4 * 4 = 921612∗6∗2∗4∗4∗4=9216
possibilities, which makes it feasible to just try them all. Specifically,
we choose two numbers (with order) in 12 ways and perform one of 4 operations
(12 * 4). Then, with 3 remaining numbers, we choose 2 of them and perform one
of 4 operations (6 * 4). Finally we have two numbers left and make a final
choice of 2 * 4 possibilities.


'''
