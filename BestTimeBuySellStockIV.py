class Solution:
    def maxProfit(self, k: 'int', prices: 'List[int]') -> 'int':
        def buyAnyTime(prices):
            res=0
            buy=False
            for i in range(len(prices)):
                if i+1<len(prices) and  prices[i+1]>prices[i]:
                    res+=prices[i+1]-prices[i]
            return res
        if not prices: return 0
        
        if k>=len(prices):
            return buyAnyTime(prices)
        
        profit=[0]*len(prices)
        
        for j in range(k):
            preprofit=0
            for i in range(1,len(prices)):
                
                current_profit=prices[i]-prices[i-1]

                #preprofit+current_profit=price[j]-price[m]
                #profit[i] = profit[m] (append in the middle)

##
##                T[i][j]=(T[i][j-1], price[j]-price[m]+T[i-1][m]
##                [3,2,6,5,0,3]
##                            at 3: current=3-0=3 + preprofit
##                            preprofit at 0 is profit[0] (T[i-1][m])
##                [0, 0, 4, 4, 4, 4]
##                [0, 0, 4, 4, 4, 7]
                preprofit=max(profit[i],preprofit+current_profit)
                
                #buy or not transaction
                profit[i]=max(profit[i-1],preprofit)
            
            
        return profit[-1]
        
        
        
'''

https://www.youtube.com/watch?v=oDhu5uGq_ic
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
    discuss/54131/Well-explained-Python-DP-with-comments

    

'''
    
