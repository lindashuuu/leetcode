class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        
        if not citations: return 0
        citations=sorted(citations, reverse=True)
        result=0
        for i in range(len(citations)):
            if citations[i]>=i+1:
                result=i+1
            else:
                break
        
        return result
