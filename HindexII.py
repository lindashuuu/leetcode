class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        if not citations: return 0
        left,right=0,len(citations)-1
        
        while left<=right:
            
            mid=(left+right)//2
            
            if citations[mid]<len(citations)-mid:
                left=mid+1
            else:
                
                
                if mid-1>=0 and citations[mid-1]>=len(citations)-mid:
                    right=mid-1
                    
                else:
                    
                    return len(citations)-mid
         
        return len(citations)-left
        
'''
    left<right don't work for [0] (doesn't check one element)

'''
