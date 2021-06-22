#Medium -- https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix/0



arr =  [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10,11,12],
        [13,14,15,16]]
r = 4
c = 4

rr = 0
ll = r
dd = c
uu = 0

res = []

while True:

    for i in range(uu,dd):
        res.append(arr[rr][i])
    rr += 1

    if ll == rr:
        break

    for i in range(rr,ll):
        res.append(arr[i][dd-1])
    dd = dd-1

    if uu == dd:
        break

    temp = []
    for i in range(uu,dd):
        temp.append(arr[ll-1][i])
    res += temp[::-1]
    ll = ll-1

    if ll == rr:
        break

    temp = []
    for i in range(rr,ll):
        temp.append(arr[i][uu])
    res += temp[::-1]
    uu += 1
    if ll == rr or uu == dd:
        break

print(res)

