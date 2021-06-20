#Medium -- https://practice.geeksforgeeks.org/problems/trapping-rain-water/0

arr = [8,8,2,4,5,5,1]
n = len(arr)

lm = 0
rm = 0
l = 0
r = n-1
cnt = 0

while (l<r):
    lm = max(lm,arr[l])
    rm = max(rm,arr[r])
    if lm < rm:
        cnt += lm - arr[l]
        l+= 1
    else:
        cnt += rm - arr[r]
        r -= 1


print(cnt)
