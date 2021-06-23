#Medium -- https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1#


def pal(ss,i,j):
    l = i-1
    r = j+1
    while l >= 0 and r < len(ss) and ss[l] == ss[r]:
        l = l-1
        r = r+1
    return ss[l+1:r]


ss = 'aaaabbaa'

if len(ss) < 2:
    print(ss)
else:
    mx = ''
    for i in range(len(ss)-1):
        tt = pal(ss,i,i)
        if len(tt) > len(mx):
            mx = tt
        if ss[i] == ss[i+1]:
            tt = pal(ss,i,i+1)
            if len(tt) > len(mx):
                mx = tt


    print(mx)



