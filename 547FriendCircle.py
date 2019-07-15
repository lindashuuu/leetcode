class Solution(object):
    
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N=len(M)
        parent ={i:i for i in range(len(M))}
        rank =[1]*N 
        self.count=N*N
       
        def find(x):
           
            if parent[x] != x:
                parent[x]=find(parent[x])
           
            return parent[x]
        
        def union(x,y):
           
            rootX=find(x)
            rootY=find(y)
            if rootX != rootY:
                less, more =((rootX,rootY) 
                            if rank[rootX]<rank[rootY]
                            else (rootY,rootX))
                parent[less] = more
                rank[more]+=rank[less]
               
                self.count-=1
             
        for i in range(N):
            for j in range(i+1,N):
                if M[i][j]==1:
                    union(i,j)
                    
                    
        return sum([1 for k, v in parent.items() if k == v])
