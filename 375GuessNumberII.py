class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dp(table,start,end):
            if(start>=end):
                return 0
            if table[start][end]>0:
                return table[start][end]
            result=sys.maxsize
            for i in range(start,end+1):
                temp=i+max(dp(table,start,i-1), dp(table,i+1,end))
                result=min(result,temp)
            table[start][end]=result
            return result
        table=[[0 for i in range(n+1)] for j in range(n+1)]
        return dp(table,1,n)
    
'''
dp[i][j] is the minimal cost to guess from range(i...j).
When you choose an x where i <= x <= j, you may find the target number
from left i...x-1, or you may find the target number from the x+1...j, because
you don't know which way should go, so to guarantee you have enough money to find the target,
you need to prepare the more, which is max(dp[i][x-1], dp[x+1][j]).
'''
