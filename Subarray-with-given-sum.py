#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1#

n = 5               #length of array
s = 12              #sum to be found
arr = [1,2,3,7,5]   #array

dic = {0:-1}
z = 0

for i in range(n):
    z += arr[i]

    if z-s in dic:
        print(dic[z-s]+2,i+1)
        break

    dic[z] = i

