class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        node_set = set(i for i in range(n))
      
        parent = {num:num for num in node_set}
        
        def find(x):
            if parent[x]==x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY: return
            parent[rootX]= parent[rootY]
            
        for x,y in edges:
             union(x,y)
        return len({find(x) for x in parent})
'''
One remark is that this Union-Find algorithm uses Union by rank,
otherwise the time complexity is O(log(N)) for each merge.
Only with both Union by rank and path compression,
we have ~O(1) time for each union/find operation,
so it gives O(V + E) time in total.

'''
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        node_set = set(i for i in range(n))
      
        parent = {num:num for num in node_set}
        rank = [1] * n
        def find(x):
            if parent[x]==x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY: return
            less, more = ((rootX,rootY) if rank[rootX]<rank[rootY] else (rootY,rootX))
            parent[less]= parent[more]
            rank[more]+=rank[less]
            
        for x,y in edges:
             union(x,y)
        return len({find(x) for x in parent})
