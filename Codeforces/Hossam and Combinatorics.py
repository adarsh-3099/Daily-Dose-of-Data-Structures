"""
Firstly, let's find max1≤𝑝,𝑞≤𝑛|𝑎𝑝−𝑎𝑞|=𝑚𝑎𝑥(𝑎)−𝑚𝑖𝑛(𝑎)
if it's equal to zero, then any pair is valid, so answer if 𝑛⋅(𝑛−1)
Otherwise, let's calculate 𝑐𝑜𝑢𝑛𝑡_𝑚𝑖𝑛 and 𝑐𝑜𝑢𝑛𝑡_𝑚𝑎𝑥. Answer is 2⋅𝑐𝑜𝑢𝑛𝑡_𝑚𝑖𝑛⋅𝑐𝑜𝑢𝑛𝑡_𝑚𝑎𝑥
"""

n = int(input())
while n > 0:
    x = int(input())
    li = [int(_) for _ in input().split()]
    minNum = min(li)
    maxNum = max(li)
    maxD = max(li) - min(li)
    if maxD == 0:
        print(x*(x-1))
    else:
        minC = 0
        maxC = 0
        for i in li:
            if i == minNum:
                minC += 1
            if i == maxNum:
                maxC += 1
        print(2*minC*maxC)
    n -= 1
        
