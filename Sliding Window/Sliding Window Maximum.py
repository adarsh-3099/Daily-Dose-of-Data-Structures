class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        
        if k == 1:
            return A

        res = []
        dq = []

        for i in range(len(A)):
            if dq and dq[0] == i-k:
                dq.pop(0)

            while dq and A[dq[-1]] < A[i]:
                dq.pop()

            dq.append(i)

            if i >= k-1:
                res.append(A[dq[0]])

        return res