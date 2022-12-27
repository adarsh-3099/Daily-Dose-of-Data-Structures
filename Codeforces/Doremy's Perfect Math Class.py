""" Find GCD of every number """

n = int(input())
while n > 0:
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a%b)

    x = int(input())
    li = [int(_) for _ in input().split()]
    tmp = 0
    for i in li:
        tmp = gcd(tmp, i)
    print(li[-1]//tmp + (li[0] == 0))
    n -= 1