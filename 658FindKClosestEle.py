class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start,end=0,len(arr)-k
        while start<end:
            mid=(start+end)//2
            if (x-arr[mid]>arr[mid+k]-x):
                start=mid+1
            else:
                end=mid
        return arr[start:start+k]



'''
compare
               x
[mid]---k---[mid+k-1] [mid+k]

'''
