n = int(input())
res = 0
while n>0:
    li = [int(i) for i in input().split(" ")]
    s = sum(li)
    if s >= 2:
        res += 1
    n -= 1
print(res)