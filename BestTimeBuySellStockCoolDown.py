class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
 #brute force       
        N=len(prices)
        if not prices:return 0
        rest,hold,sold=[0]*N,[0]*N,[0]*N
        hold[0]=-prices[0]
        for i in range(1,N):
            rest[i]=max(rest[i-1],sold[i-1])
            sold[i]=hold[i-1]+prices[i]
            hold[i]=max(hold[i-1],rest[i-1]-prices[i])
        
        return max(sold[-1],rest[-1])

'''
               rest(not buy)
                   \
buy(-price)       / rest\
                /        \
               hold --- sold
              /     sell(+price)

        hold(not sell)

        https://www.youtube.com/watch?v=oL6mRyTn56M
'''


'''
because we only care about answer right before i , space can be O(1)

class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        
        N=len(prices)
        if not prices:return 0
        rest,hold,sold=0,-prices[0],0
      
        for i in range(1,N):
            temp=rest
            rest=max(rest,sold)
            sold=hold+prices[i]
            hold=max(hold,temp-prices[i])
        
        return max(sold,rest)

O(N) O(1)
'''
