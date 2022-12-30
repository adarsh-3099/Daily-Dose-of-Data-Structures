class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, n):
        
        board=[['.' for i in range(n)]for j in range(n)]
        self.ans=[]
        self.solve(0,0,board)
        return self.ans
    def issafe(self,row,col,board):
        drow=row
        dcol=col
        while col>=0 and row>=0:
            if board[row][col]=='Q':
                return False
            row-=1
            col-=1
        row=drow
        col=dcol
        while col>=0:
            if board[row][col]=='Q':
                return False
            col-=1
        row=drow
        col=dcol
        while row<len(board) and col>=0:
            if board[row][col]=='Q':
                return False
            row+=1
            col-=1
        return True
    def solve(self,row,col,board):
        if col==len(board):
            self.ans.append(["".join(board[i]) for i in range(len(board))])
            return
        for row in range(len(board)):
            if self.issafe(row,col,board):
                board[row][col]='Q'
                self.solve(0,col+1,board)
                board[row][col]='.'
        return
        