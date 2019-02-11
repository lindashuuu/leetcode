class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        maxi=0
        mini=sys.maxsize
        
        if not prices:return 0
        
        for i in prices:
            maxi=max(maxi,i-mini)
            mini=min(i,mini)
        return maxi


'''
    time:O(N)
    space: O(1)

'''
