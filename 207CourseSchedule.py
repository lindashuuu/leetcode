class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 1 : return True
        par = [0] * (numCourses)
        child = [[] for i in range(numCourses)]
        for i , j in prerequisites:
            par[i]+=1
            child[j].append(i)
 
        leaves = [i for i in range(numCourses) if not par[i]]   
        while len(leaves):
            numCourses-=len(leaves)
            new_leaves=[]
            for leave in leaves:
                for c in child[leave]:
                    par[c]-=1
               
                    if not par[c]:
                        new_leaves.append(c)
            leaves = new_leaves
        return numCourses==0
'''
toplogical sort
O(V + E) time and O(V + E) space

'''
