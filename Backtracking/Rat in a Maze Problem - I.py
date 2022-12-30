class Solution:
    def findPath(self, m, n):
        # code here
        res = []
        def solve(m,s,n,i,j,res):
            if i==n-1 and j==n-1:
                res.append(s)
                return
            if(i>=0 and j>=0 and i<n and j<n and m[i][j]):
                m[i][j] = 0
                solve(m,s+'D',n,i+1,j,res)
                solve(m,s+'L',n,i,j-1,res)
                solve(m,s+'R',n,i,j+1,res)
                solve(m,s+'U',n,i-1,j,res)
                m[i][j] = 1
            return
        
        if(m[0][0]!=0 or m[n-1][n-1]!=0):
                solve(m,"",n,0,0,res)
        return res