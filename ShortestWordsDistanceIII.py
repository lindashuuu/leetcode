class Solution:
    def shortestWordDistance(self, words: 'List[str]', word1: 'str', word2: 'str') -> 'int':
        index=-1
        res=sys.maxsize
        
        for i in range(len(words)):
            
            if words[i]==word1 or words[i]==word2:
                if index!=-1 and ((words[i]!=words[index]) or (index!=i and word1==word2)):
                    res=min(res,abs(i-index))
                index=i
                
        return res
'''
    O(N)
    the same as version 1 but one more different condition 


'''
