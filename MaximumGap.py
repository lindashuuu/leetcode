'''

sum of gap is (max-min)

we have n-1 gap , so maximum must be greater than (max-min)/(n-1)
so we don't need to check number inside bucket

be careful of len_bucket (might be 0)

'''
class Solution:
    def maximumGap(self, nums: 'List[int]') -> 'int':
        if len(nums)<2: return 0
        
        maxi,mini=-sys.maxsize,sys.maxsize
        for i in nums:
            maxi=max(maxi,i)
            mini=min(mini,i)
            
        if maxi-mini==0: return 0
        
        len_bucket=((maxi-mini)//(len(nums)-1)) or 1
        
       
        num_bucket = [[None, None] for _ in range((maxi-mini)//len_bucket+1)]
        
        for i in nums:
           
            b=num_bucket[(i-mini)//len_bucket]
            b[0]=(i if b[0]==None else min(i,b[0]))
            b[1]=(i if b[1]==None else max(i,b[1]))
        
        gap=-sys.maxsize
        prev=0
        for i in range(len(num_bucket)):
            if num_bucket[i][0]==None: continue
            else:
                gap=max(gap,num_bucket[i][0]-num_bucket[prev][1])
                prev=i
            
        return gap
        
