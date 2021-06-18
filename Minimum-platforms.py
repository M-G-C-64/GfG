#Medium -- https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

arr.sort()
dep.sort()

mxpl = 1
j = 0
for i in range(1,n):
    if arr[i] <= dep[j]:
        mxpl += 1
    else:
        j += 1

print(mxpl)
