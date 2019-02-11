class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        
        res=0
        buy=False
        for i in range(len(prices)):
            if i+1<len(prices) and prices[i+1]>=prices[i] and not buy:
                res-=prices[i]
                buy=True
            elif ((i+1<len(prices) and prices[i+1]<prices[i]) or i==len(prices)-1) and buy:
                res+=prices[i]
                buy=False
                
                
        
        return res
'''

    improve:
     if (prices[i] < prices[i + 1]) {
                res += prices[i + 1] - prices[i];
            }


    For example, given {5, 1, 2, 3, 4},
    buy at 1 & sell at 4 is the same as
    buy at 1 &sell at 2 & buy at 2& sell at 3 & buy at 3 & sell at 4.
    
    basically find increasing sequences
    
    time: O(N)
    space:O(1)

'''
