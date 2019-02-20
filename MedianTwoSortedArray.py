class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        len1,len2=len(nums1),len(nums2)
        if len1>len2:
            return self.findMedianSortedArrays(nums2,nums1)
       
        left,right=0,len1
        
        while (left<=right):
            partitonX=(left+right)//2
           
            partitonY=(len1+len2+1)//2-partitonX
            
            leftMin=nums1[partitonX-1] if (partitonX)!=0 else -sys.maxsize
            rightMin=nums1[partitonX] if (partitonX)!=len1 else sys.maxsize
            
            leftMax=nums2[partitonY-1] if (partitonY)!=0 else -sys.maxsize
            rightMax=nums2[partitonY] if (partitonY)!=len2 else sys.maxsize
            
            if leftMin<=rightMax and leftMax<=rightMin:
                if (len1+len2)%2:
                    return max(leftMin,leftMax)
                else:
                    
                    return (max(leftMin,leftMax)+min(rightMin,rightMax))/2
                
            elif leftMax>rightMin:
                left=partitonX+1
            else:
                right=partitonX-1
            
                
                
        return -1
'''
https://www.youtube.com/watch?v=LPFhl65R7ww&t=273s

O(log min(M,N)), O(1)

'''
