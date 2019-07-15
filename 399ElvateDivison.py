class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        Given the number of variables N, and number of equations E,
building the graph takes O(E), each query takes O(N+E), space for graph takes O(E)

Regarding the time complexity, if there are m queries, q equations and n distinct values, the without optimization,
by definition of BFS, it will be O(m(q+n)) ~ O(m * n^2) q can grow to n^2
        """
        graph={}
        def build_graph(equations,value):
            def add_edge(src,dest,value):
                if src not in graph:
                    graph[src]=[(dest,value)]
                else:
                    graph[src].append((dest,value))
            
            for eq in range(len(equations)):
                src,dest=equations[eq][0],equations[eq][1]
                value=values[eq]
                add_edge(src,dest,value)
                add_edge(dest,src,1/value)
                
        def bfs(src,dest):
            if src not in graph or dest not in graph:
                return -1.0
            visited=set()
            
            queue=[(src,1.0)]
            while queue:
                neightbor, value=queue.pop(0)
                if neightbor == dest:
                    return value
                visited.add(neightbor)
                for i,v in graph[neightbor]:
                        if i not in visited:
                            queue.append((i,value*v))
            return -1.0

        
            
            
        build_graph(equations,values)
        return [bfs(src,dest) for src, dest in queries]
'''
union-find solution
Time complexity is 0(e + q) where e is the number of equations and q is the number of queries since Union and find operations
could be considered constant time if using rank and path compression
'''
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        alphabet = set(sum(equations,[]))
        parent={ char:char for char in alphabet}
        val ={char:1.0 for char in alphabet}
        
        def find(x):
            if parent[x]==x:
                return parent[x],val[x]
            else:
                parent[x],value = find(parent[x])
                val[x]*=value
            return parent[x],val[x]
        
        def union(y,x,value):
            rootX,valX = find(x)
            rootY,valY = find(y)
            if rootX == rootY: return
            parent[rootY] = parent[rootX]
            val[rootY] = value * valX/valY
            
        for (y, x), value in zip(equations, values):
            union(y, x, value)
        res = []
        for y, x in queries:
            if x not in alphabet or y not in alphabet: 
                res.append(-1.0)
                continue
            y, valy = find(y)
            x, valx = find(x)
            if x == y: res.append(valy / valx)
            else: res.append(-1.0)
        return res
