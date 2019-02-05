from collections import defaultdict
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull,cow=0,0
        count=defaultdict(int)
        for i in range(len(secret)):
                if secret[i]==guess[i]:
                    bull+=1
                else:
                    if count[secret[i]]<0:
                        cow+=1
                    if count[guess[i]]>0:
                        cow+=1
                    count[secret[i]]+=1;
                    count[guess[i]]-=1;
                
                
        return str(bull)+"A"+str(cow)+"B"


'''

    use hashmap and one pass to keep count of bull and cow
    when it's 0 it means there's no overlap

'''
