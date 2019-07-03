class Solution:
    def helper(self,nums,target,closed):
        start,end=0,len(nums)-1 
      
        while start<=end:
            middle=(start+end)//2
            
            if nums[middle]==target :
               
                return middle
            if (closed and nums[middle]<target and
                middle+1<len(nums) and nums[middle+1] > target):
                return middle
            if (nums[middle]>target):
                end=middle-1
            else:
                start=middle+1
        return -1
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:return False
        firstELementInRows=[matrix[n][0] for n in range(len(matrix))]
        ## O(R) you don't need to initialize this array and it can be faster!
        rowIndex=self.helper(firstELementInRows,target,True)
        colIndex=self.helper(matrix[rowIndex],target,False)
       
        if colIndex==-1:
            return False
        return True
        
##### sol2
class Solution:
    '''
    a[x][y]=a[x*r+y]
    a[?]=a[x//r][x%r] --- r=number of columns!
    '''
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:return False
        start,end=0,(len(matrix)*len(matrix[0])-1)
      
        while start<=end:
            middle=(start+end)//2
         
            if matrix[middle//len(matrix[0])][middle%len(matrix[0])]==target:
                return True
            elif matrix[middle//len(matrix[0])][middle%len(matrix[0])]>target:
                end=middle-1
            else:
                start=middle+1
        return False
            
            
                   
            
'''
 Be careful of the edge case like [[]] , need to check for matrix[0]
'''
