class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)< 3:
            return len(points)
        
        maxi = 2
        
        for i in range(1,len(points)):
            count=0
            x1,y1=points[i-1]
            x2,y2 = points[i]
            if x1==x2 and y1==y2:
                for x3,y3 in points:
                    if x1 == x3 and y1 == y3:
                        count+=1
            else:
                for x3,y3 in points:
                    if (y3-y2)*(x2-x1) == (y2-y1)*(x3-x2):
                        count+=1
            
            
            maxi=max(count,maxi)
        
        
        
        return maxi
