class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        i = j = 0
        r = 0
        ans = 0
        while j < len(s):
            r += abs(ord(s[j]) - ord(t[j]))
            if r < maxCost:
                ans = max(ans, j-i+1)
                j += 1
            else:
                while r > maxCost and i <= j:
                    r -= abs(ord(s[i]) - ord(t[i]))
                    i += 1
                ans = max(ans, j-i+1)
                j += 1
        return ans