import heapq

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        res = []
        heapq.heapify(A)
        for i in range(len(A)-B+1):
            heapq.heappop(A)
        return A