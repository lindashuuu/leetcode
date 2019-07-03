class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not list:
            return -1
        start,end=0,len(nums)-1
        while(start<=end):
            middle=(start+end)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                end=middle - 1
            else:
                start=middle+1
        
        
        
        return -1
    

'''
https://leetcode.com/problems/binary-search/
not pass: 
[5] 5
start,end=0
find 4
[1,2,3] 4
middle = 2
start=3, end =3



//[1,2,3]
// 0 1  2
find 1:
    middle=0+2//2=1
    end=1
    
    middle=(0+1)//2==0
    find
    
find 3:
    middle=2+2//2=2
    start=1
    
    middle=(2+1)//2==0
    find
'''
