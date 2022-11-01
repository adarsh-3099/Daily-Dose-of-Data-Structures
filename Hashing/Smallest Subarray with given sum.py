def subArraylen(arr, n, K):
    mp = defaultdict()
    currPrefixSum = 0
    result = sys.maxsize
    for i in range(n):
	    currPrefixSum += arr[i]
	    if(currPrefixSum == K):
		    currLen = i + 1
		    result = min(result, currLen)
	    requirePrefixSum = currPrefixSum - K

	    if(requirePrefixSum in mp.keys()):
		    foundIdx = mp[requirePrefixSum]
		    currIdx = i
		    result = min(result, currIdx - foundIdx)

	    mp[currPrefixSum] = i
    return result
