from collections import defaultdict
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def add_edge(i,j,graph,indegree):
            if j not in graph[i]:
              
                graph[i].add(j)
                indegree[ord(j)-ord('a')]+=1

        def bfs(graph,indegree):
            result=""
            queue=[]
         
            for key in graph:
                if indegree[ord(key)-ord('a')] == 0:
                    queue.append(key)
                    result+=key
            while queue:
                element = queue.pop(0)
                
                for out in graph[element]:
                    indegree[ord(out)-ord('a')]-=1
                    if not indegree[ord(out)-ord('a')]:
                        queue.append(out)
                        result+=out
            return result
        
        graph = dict()
        indegree = [0]*26
        for i in range(len(words)):
            second = words[i]
            for c in second:
                graph[c]=set() ##must have, or not added to edge would not loop
                ##['z','z']
        for i in range(1,len(words)):
            first = words[i-1]
            second = words[i]
           
            for j in range(min(len(first),len(second))):
                if first[j] != second[j]:
                    add_edge(first[j],second[j],graph,indegree)
                    break
        result=bfs(graph,indegree)
       
        if len(result) ==  len(graph):
            return result
        else:
            return ""
