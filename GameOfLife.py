class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        # 00
        # 01
        # 10
        # 11
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                lives=0
                #3*3  x[i][j]
                
                for k in range(max(0,i-1),min(len(board),i+2)):
                    for m in range(max(0,j-1),min(len(board[0]),j+2)):
                        lives+=(board[k][m] & 1) #different than and
          
                if lives==3 or lives-board[i][j]==3:
                    if board[i][j]==0:
                        board[i][j]=2
                    else:
                        board[i][j]=3
        print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]=board[i][j]>>1
'''
https://www.youtube.com/watch?v=juGxbF-eadU
O(9MN)=O(MN) O(1)



'''
