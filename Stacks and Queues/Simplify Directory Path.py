class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        li = []
        A = A.split("/")
        i = 0
        n = len(A)
        while i < len(A):
            while i == " ":
                i += 1
            if A[i].isalpha():
                li.append(A[i])
            if A[i] == "..":
                if li:
                    li.pop()
            i += 1
                
        if len(li) == 0:
            return "/"
        res = ""
        for i in li:
            res += "/"+i
        return res