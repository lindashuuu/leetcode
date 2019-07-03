"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        
        queue=[node]
        visited=dict()
        temp=Node(node.val,[])
        visited[node.val]=temp
        while queue:
            new_node=queue.pop()
            for i in new_node.neighbors:
                if i.val not in visited:
                    visited[i.val]=Node(i.val,[])
                    queue.append(i)
                    
                visited[new_node.val].neighbors.append(visited[i.val])
                
        return temp
