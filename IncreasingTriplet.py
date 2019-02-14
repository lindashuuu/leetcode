class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> 'bool':
        m1,m2=sys.maxsize,sys.maxsize
        for i in nums:
            if i<=m1:
                m1=i
            elif i<=m2:
                m2=i
            else:
                return True
            
        return False



'''
    similar to find the third maximum in a array

    m1<m2<X

    i<m1 and i<m2
    if i==m1 would be true, update m2=m1


'''
