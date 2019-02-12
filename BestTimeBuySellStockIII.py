class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        buy1,buy2,sell1,sell2=-sys.maxsize,-sys.maxsize,0,0
        for i in prices:
            if buy1<-i:
                buy1=-i
            
            if sell1<i+buy1:
                sell1=i+buy1
            
            if buy2<sell1-i:
                buy2=sell1-i
                
            if sell2<buy2+i:
                sell2=buy2+i
                
        
        return sell2


'''

    O(N)
    O(1)
    
    b1,s1 is simple
    b2,s2 keep tracks of the second transaction where it's maximum

    

'''
