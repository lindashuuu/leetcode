class Solution:
    def majorityElementII(self, nums: 'List[int]') -> 'List[int]':
        result=[]
        if not nums:return result
        posM,posN=0,0
        cm,cn=0,0
        for i in range(len(nums)):
            if nums[i]==nums[posM]:
                    cm+=1
                    
            elif nums[i]==nums[posN]:
                    cn+=1
 
            elif cm==0:
                posM=i
                cm=1
            elif cn==0:
                posN=i
                cn=1
            else:
                cn-=1
                cm-=1
                
        
        cn,cm=0,0
        for i in nums:
            if i==nums[posM]:
                cm+=1
            elif i==nums[posN]:
                cn+=1
        
        if cm>len(nums)//3:
            result.append(nums[posM])
        if cn>len(nums)//3:
            result.append(nums[posN])
        return result
                

        
