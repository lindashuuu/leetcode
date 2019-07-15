class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        if numCourses == 1 : return [0]
        par = [0] * (numCourses)
        child = [[] for i in range(numCourses)]
        for i , j in prerequisites:
            par[i]+=1
            child[j].append(i)
 
        leaves = [i for i in range(numCourses) if not par[i]] 
        result=[]
        n = numCourses
        while len(leaves):
            numCourses-=len(leaves)
            result.extend(leaves)
            new_leaves=[]
            for leave in leaves:
                for c in child[leave]:
                    par[c]-=1
               
                    if not par[c]:
                        new_leaves.append(c)
            leaves = new_leaves
    
        if len(result) == n:
   
            return result
        else:
            return []
