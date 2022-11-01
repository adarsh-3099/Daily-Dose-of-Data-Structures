def count_fre(arr):
    m = {}
    for i in arr:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    return m