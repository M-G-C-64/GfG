#EASY -- https://practice.geeksforgeeks.org/problems/equilibrium-point/0

su = sum(A)
fs = 0
ls = su
if N <= 1:
  return 1
if su-A[0] == 0:
  return 1
for i in range(1,N):
  fs += A[i-1]
  ls = su - fs - A[i]
  if fs == ls:
      return i+1
return -1
