class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> 'int':
        count=set()
        for i in nums:
            count.add(i)
            
        longest=0
        for i in nums:
            down=i-1
            up=i+1
            if i not in count: continue
                
                
            while down in count:
                count.remove(down)
                down-=1
            while up in count:
                count.remove(up)
                up+=1
            longest=max(longest,up-down-1)
            
            
        return longest

'''
O(N) becasue the while loop run once
 the while loop can only run for
 n iterations throughout the entire runtime of the algorithm.
O(N) 


'''
