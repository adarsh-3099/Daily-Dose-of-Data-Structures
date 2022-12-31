class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def MAH(hist):
            nsr = [0]*len(hist)
            nsl = [0]*len(hist)
            m = {v:i for i,v in enumerate(hist)}
            n = len(hist)        
            #nsr 
            st = []
            for i in range(n-1,-1,-1):
                if not st:
                    st.append((hist[i],i))
                    nsr[i] = n
                else:
                    while st and hist[i] <= st[-1][0]:
                        st.pop()
                    x = n
                    if st:
                        val, x = st[-1]
                    st.append((hist[i],i))
                    nsr[i] = x
            #print(nsr)
            #nsl
            st = []
            for i in range(n):
                if not st:
                    nsl[i] = -1
                    st.append((hist[i],i))
                else:
                    while st and hist[i] <= st[-1][0]:
                        st.pop()
                    x = -1
                    if st:
                        val, x = st[-1]
                    nsl[i] = x
                    st.append((hist[i],i))
            #print(nsl)
            li = []
            for i in range(len(nsl)):
                li.append(nsr[i]-nsl[i]-1)
            #print(li)
            res = []
            for i in range(n):
                res.append(abs(hist[i]*li[i]))
            return max(res)
        
        if not matrix:
            return 0
        
        res = []
        n = len(matrix)
        t = [int(i) for i in matrix[0]]
        res.append(MAH(t))
        print(t)
        for i in range(1,n):
            for j in range(len(t)):
                if int(matrix[i][j])>0:
                    t[j] = t[j] + 1
                else:
                    t[j] = 0
            res.append(MAH(t))
        print(res)
        return max(res)
        