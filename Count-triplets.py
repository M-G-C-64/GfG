# ---TIP--- searching throug a dictionary is very time efficient than searching through a list
#https://practice.geeksforgeeks.org/problems/count-the-triplets4615/1#


n = 4
lst = [1,5,3,2]


lst.sort()
dic = {}
for i in range(len(lst)):
    dic[lst[i]] = i
cnt = 0

for i in range(n-1):
    for j in range(i+1,n):
        if (lst[i]+lst[j]) in dic:
            cnt += 1

print(cnt)

