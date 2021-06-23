#Medium -- https://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array/0


arr = [3, 30, 34, 5, 9]

dic = {}
for i in range(10):
    dic[str(i)] = []


for i in arr:
    dic[str(i)[0]].append(str(i))

strr = ''
for i in range(9,-1,-1):


    if len(dic[str(i)]) > 0:
        tt = -1
        for z in dic[str(i)]:
            if int(z) > tt:
                tt = int(z)
        tt = tt*2
        temp = sorted(dic[str(i)], key = lambda x: int((x*((tt//len(x))+1))[:tt]), reverse=True)
        for j in temp:
            strr += str(j)


        
#pprint.pprint(dic)
print(strr)
