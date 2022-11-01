'''
Use dictionary
	-> if element in dict then ans = max(ans, i-d[li[i]])
	-> else add element to dict; d[li[i]] = i
'''

ans = -1
d = {}
for i in range(len(li)):
   if li[i] in d:
       ans = max(ans, i-d[li[i]])
   d[li[i]] = i
print(ans)
