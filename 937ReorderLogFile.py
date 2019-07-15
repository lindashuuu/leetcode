class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]

        ics 33 sort review...
        
        """
        letter = []
        num = []
        for i in logs:
            if (i.split()[1].isnumeric()):
                num.append(i)
            else:
                letter.append(i)
                
                
        letter.sort(key = lambda x : (x.split()[1:],x.split()[0]) )
 
        return letter + num
