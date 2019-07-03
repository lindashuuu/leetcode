'''
Given an array of numbers, return true
if given array can represent preorder traversal of a Binary Search Tree,
else return false. Expected time complexity is O(n).


I don't understand the solution...

'''
def canRepresentBST(pre): 
  
    # Create an empty stack 
    s = [] 
  
    # Initialize current root as minimum possible value 
    root = -sys.maxsize
  
    # Traverse given array 
    for value in pre:  
        #NOTE:value is equal to pre[i] according to the  
        #given algo    
      
        # If we find a node who is on the right side 
        # and smaller than root, return
        #False value is the left subtree of root node
        
        if value < root : 
            return False 
      
        # If value(pre[i]) is in right subtree of stack top,  
        # Keep removing items smaller than value 
        # and make the last removed items as new root 
        while(len(s) > 0 and s[-1] < value) : 
            root = s.pop() 
          
        # At this point either stack is empty or value 
        # is smaller than root, push value 
        s.append(value) 
  
    return True
