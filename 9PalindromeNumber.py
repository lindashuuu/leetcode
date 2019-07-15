class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if not x: return True
        if x<0 or x%10 ==0 :
            return False
        arc=0
        num = x
        //20 0 2  1 1
        while num>arc:
            
            arc*=10
            arc+=num%10
            num=num//10
            print(num,arc)
        print(num,arc)
        return arc==num or arc//10 == num
        
        
        
'''
20
0 would go to the last digit, and divde it by 10 = 0

11
1 1 stop


'''
