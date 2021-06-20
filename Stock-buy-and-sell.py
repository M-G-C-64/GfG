# Medium -- https://practice.geeksforgeeks.org/problems/stock-buy-and-sell-1587115621/1#

b = -1
s = -1

res = []
for i in range(1,n):
    if A[i] > A[i-1]:
        if b == -1:
            b = i-1
        s = i
    if A[i] < A[i-1]:
        if b > -1:
            res.append((b,s))
            b = -1
if s > b and s>0 and b > -1:
    res.append((b,s))
return res
