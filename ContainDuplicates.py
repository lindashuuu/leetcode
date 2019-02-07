class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        return len(set(nums))!=len(nums)
'''
 or use dictionary:
    if it's in the dictionary: return true
    else add it to the dictionary

'''
