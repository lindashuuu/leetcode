class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        if not len(edges)==n-1:
            return False
        parent = {i:i for i in range(n)}
       
        def find(x):
            if parent[x] == x:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]
            
        for x,y in edges:
            rootX = find(x)
            rootY = find(y)
            if rootX==rootY:
                return False
            
            parent[rootX] = rootY
            
        return True
            
