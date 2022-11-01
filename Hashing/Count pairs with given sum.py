''' 
-> Create freq map and loop through array.
-> if k-i in d: count += d[k-i] as it can form as many as pair as count
'''

def getPairsCount(self, arr, n, k):
       d = Counter()
       c = 0
       for i in arr:
	       c += d.get(k-i, 0)
    	   d[i] += 1
       return c
