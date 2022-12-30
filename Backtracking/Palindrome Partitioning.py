class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        
        def func(s,suru,comb):
            if suru == len(s):
                res.append(list(comb))
                return
            
            if suru > len(s):
                return
            
            start = suru
            end = suru + 1
            while end<=len(s):
                curr = s[start:end]
                if curr == curr[::-1]:
                    comb.append(curr)
                    func(s,end,comb)
                    comb.pop()
                end += 1
            
        res = []
        comb = []
        func(A,0,comb)
        return res
