class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        if len(A) <= 1:
            return [-1]
        m = A[0]
        li = []
        for i in range(len(A)):
            while li and li[-1]>=A[i]:
                li.pop()
            x = -1
            if li:
                x = li[-1]
            li.append(A[i])
            A[i] = x
        return A
        