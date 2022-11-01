''' 
-> Make a dict and store all indexes of elements and return the element with only single element and lowest index.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        m = {}
        for i in range(len(s)):
            if s[i] in m:
                m[s[i]].append(i)
            else:
                m[s[i]] = [i]
            
        c = 2**31-1
        print(m)
        for i in m.keys():
            if len(m[i]) == 1:
                c = min(c, m[i][0])
    
        if c == 2**31-1: return -1
        return c
