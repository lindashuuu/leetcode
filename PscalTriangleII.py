class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        if rowIndex==0: return [1]
        result=[0]*(rowIndex+1)
        
        result[0]=1
        for i in range(1,rowIndex+1):
            for j in range(i,0,-1):
            
                result[j]+=result[j-1]
        
        
        
        
        return result

'''
     O(N^2) time, O(N) space,  recursion
     
    https://leetcode.com/problems/pascals-triangle-ii/discuss/
    38444/Here-is-my-O(n)-solution-and-the-proof

''''
