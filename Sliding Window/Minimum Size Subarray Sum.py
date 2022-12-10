class Solution:
    def minSubArrayLen(self, K: int, A: List[int]) -> int:
        ans = len(A)+1
        i = j = s = 0

        while j<len(A):
            s += A[j]
            print(s, ans)
            if s < K:
                j += 1
            else:
                while s >= K and j >= i:
                    ans = min(ans, j-i+1)
                    s -= A[i]
                    i += 1
                j += 1

        if ans == len(A)+1:
            return 0
        return ans