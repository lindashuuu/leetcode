class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
       
     
        parent = dict()
        result=[]
        count = 0
        
        def find(x):
            if parent[x]==x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y,count):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY: 
                return count
            parent[rootX]= parent[rootY]
           
            return count-1
        
        
        for po1,po2 in positions:
           
            index = po1*n+po2
            if index not in parent:
                parent[index] = index
                count+=1
            for di in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = po1+di[0], po2+di[1]
                if 0 <= x < m and 0 <= y < n and x*n+y in parent:
                    count = union(index, x*n+y,count)
            result.append(count)
        
        
        return result
