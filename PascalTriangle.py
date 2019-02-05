class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result=[]
        if numRows==0: return result
        result.append([1])
        for i in range(1,numRows):
            temp=[1]
            for j in range(1,i):
                left,right=j-1,j
                temp.append(result[i-1][left]+result[i-1][right])
            temp.append(1)
            result.append(temp)
        
        
        
        
        return result

'''
    time complexity:
        O(numRow^2)

'''
