class Solution:
    def shortestDistance(self, words: 'List[str]', word1: 'str', word2: 'str') -> 'int':
        
        
        index=-1
        shortest=sys.maxsize
        for i in range(len(words)):
            if words[i]==word1 or words[i]==word2:
                if index!=-1 and words[index]!=words[i]:
                    shortest=min(shortest,abs(i-index))
                index=i
        
        
        return shortest



'''

     [ 2 2 3 3]
         

     [2      3  2]

     
     only update shortest when there it meets different words
     

'''
