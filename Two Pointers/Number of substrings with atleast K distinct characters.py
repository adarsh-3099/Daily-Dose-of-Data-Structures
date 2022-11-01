'''  
-> Efficient approach is to use sliding window.
-> Take start = end = 0 and a dict() as well and run loop till end<len(str)
-> while end<len(s):
	D[s[end]] += 1
	while (len(d) >= k):
		ch = d[start]
		d[ch] -= 1
		if d[ch] == 0:
			d.pop(ch)
		res += len(s) - end + 1
		Start += 1
'''

def atleastkDistinctChars(s, k):
   n = len(s)

   mp = defaultdict(int)
 
   begin = 0
   end = 0

   ans = 0
 
   while (end < n):
 
       c = s[end]
       mp += 1
 
       end += 1

       while (len(mp) >= k):
 
           pre = s[begin]
           mp[pre] -= 1
 
           if (mp[pre] == 0):
               del mp[pre]
 
           ans += len(s) - end + 1
           begin += 1
 
   print(ans)
