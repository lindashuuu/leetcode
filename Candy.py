class Solution:
    def candy(self, ratings: 'List[int]') -> 'int':
        result=[1]*len(ratings)
        
        for i in range(len(ratings)):
            if i+1<len(ratings) and ratings[i+1]>ratings[i]:
                result[i+1]=result[i]+1
        
        for i in range(len(ratings)-1,-1,-1):
            if i-1>=0 and ratings[i-1]>ratings[i]:
                result[i-1]=max(result[i]+1,result[i-1])
                
                
        return sum(result)


'''

 loop twice
     O(N)
     O(N)
'''
