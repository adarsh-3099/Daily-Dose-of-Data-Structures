class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(c, i, j):
            for r in range(9):
                if self.b[i][r] == str(c):
                    return False
                
                if self.b[r][j] == str(c):
                    return False
                
                if self.b[3*(i//3 )+ r//3][3*(j//3)+ r%3] == str(c):
                    return False
                
            return True    
            
        
        def solve():
            for i in range(9):
                for j in range(9):
                    if self.b[i][j] == ".":
                        
                        for c in range(1,10):
                            if isValid(c,i,j):
                                self.b[i][j] = str(c)
                                
                                if solve() == True:
                                    return True
                                else:
                                    self.b[i][j] = "."
                        
                        return False
            return True
                
        self.b = board
        solve()
        return self.b
        