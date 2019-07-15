class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        most inner nodes
        """
        
        if n ==1 : return [0]
        adj = [set() for i in range(n)]
        for i , j in edges:
            adj[i].add(j)
            adj[j].add(i)
        leaves = [i for i in range(len(adj)) if len(adj[i])==1]   
        while n>2:
            n-=len(leaves)
            new_leaves=[]
            for leave in leaves:
                j = adj[leave].pop()
                adj[j].remove(leave)
                if len(adj[j])==1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves
'''
find most inner nodes O(N)
V = n, E = n-1.

https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts

'''
