class Solution(object):
    def 134(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost)>sum(gas):
            return -1
        temp=[0]*len(gas)
        for i in range(len(gas)):
            temp[i]=gas[i]-cost[i]
        total=0
        position=0
        for i in range(len(temp)):
            total+=temp[i]
            if total<0:
                total=0
                position=i+1
        return position
'''
    from i to j , if i cannot reach j, then any inner points from i to j cannot reach j
    
    
    sum(gas)> sum(cost) means there will be a solution, so we can set total=0
    
    
'''
