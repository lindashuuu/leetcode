from collections import defaultdict
class WordDistance:

    def __init__(self, words: 'List[str]'):
        self.dict={}
        for i in range(len(words)):
            self.dict.setdefault(words[i],[]).append(i)
            
        print(self.dict)

    def shortest(self, word1: 'str', word2: 'str') -> 'int':
        i,j=0,0
        res=sys.maxsize
        while i<len(self.dict[word1]) and j<len(self.dict[word2]):
            res=min(res,abs(self.dict[word1][i]-self.dict[word2][j]))
            if self.dict[word1][i]<self.dict[word2][j]:
                    i+=1
            else:
                j+=1
            
        return res
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

''''
    O(M+N)
    [1,3]
       i 
    
    [2,4]
       j

'''
