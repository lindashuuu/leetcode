from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small=[]
        self.large=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small)== len(self.large):
            larger = heappushpop(self.small, -num)
            heappush(self.large, - larger)
        else:
            heappush(self.small, -heappushpop(self.large, num))
            
            
            
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small)< len(self.large):
            return self.large[0]
        else:
            return (self.large[0] - self.small[0]) / 2.0

'''
small and large heap
put number in and pop out 
large has one extra



'''

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
