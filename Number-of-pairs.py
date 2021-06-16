#partially correct
#https://practice.geeksforgeeks.org/problems/number-of-pairs/0/

import bisect

def tt(arr,ch):
    return bisect.bisect(arr,ch)


a = [2,1,6]
b = [1,5]

b.insert(0,-1)
a.sort()
b.sort()

M = len(a)
N = len(b)

dic = {-1:0,0:0,1:0,2:0,3:0}
for i in range(1,N):
    if b[i] in dic:
        dic[b[i]] += 1
    else:
        dic[b[i]] = 1

##print(dic)

sdic = {-1:0}
temp = 0
for i in dic.keys():
    sdic[i] = dic[i]+temp
    temp = sdic[i]

##print(sdic)

cnt = 0
for i in range(M):
    ff = a[i]
#if 0 -- pass
    if a[i] == 0:
        ff = -1
        pass
#if 1 -- no of 0's
    elif a[i] == 1:
        ff = -1
        cnt += dic[0]
#if 2 -- no of 0's, 1's and numbers >= 5
    elif a[i] == 2:
        ff = 4
#if 3 -- no of 0,1,2 and numbers >= 4
    elif a[i] == 3:
        cnt += dic[2]
        ff = 3
#if anb -- no of 0,1 and numbers >= anb+1
    if ff < 0:
        pass
    else:
        cnt += dic[0]+dic[1]
        #return the number just lower than a[i] in b and len(b)-sdic[aaa]
        upbnd = tt(b,ff)
        cnt += (N-1)-sdic[b[upbnd-1]]

print(cnt)

