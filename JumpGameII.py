class Solution:
    def jump(self, nums: 'List[int]') -> 'int':
        res=0
        last=0
        maxi=0
        for i in range(len(nums)):
            if i>last:
                last=maxi
                res+=1
            maxi=max(maxi,i+nums[i])
        return res


'''
Greedy algorithm
    everytime we are finding the maximum range from the current range
    O(N), O(1)

'''
