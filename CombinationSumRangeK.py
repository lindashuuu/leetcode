# Program to find the number of ways, n can be 
# written as sum of two or more positive integers in the range k
  
# Returns number of ways to write n as sum of 
# two or more positive integers
#O(N^2)


def CountWays(n,k):
    table=[0]*(n+1)

    table[0]=1
    ##when value=0 only way (select none)

    for i in range(1,k+1):
        for j in range(i,n+1):
            table[j]+=table[j-i]
    ##current value=target(j) - amount(like coin value) which is i

    return table[-1]



        
    
assert CountWays(5,3)==5
