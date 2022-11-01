'''
-> Take d = {}
-> loop through array. I+j = x;  j = x-i
-> Chck if x-i in d. If yes return the pair. Else add i to d.
'''

def findPair(arr):
    d = {}
    for i in arr:
        if x-i in d:
	        return [i,x-i]
        d[i] = 1

    
