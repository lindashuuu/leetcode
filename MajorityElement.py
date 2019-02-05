class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        position=0
        count=0
        for i in range(len(nums)):
            if count==0:
                position=i
                count=1
            else:
                if nums[i]==nums[position]:
                    count+=1
                else:
                    count-=1
           
        return nums[position]
            
'''
    Moore's Voting Algorithm (proof)
    https://neolzs.wordpress.com/2016/02/01/
    boyer-moore-majority-vote-algorithm-a-simple-proof/


'''
