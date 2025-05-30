import re

#输入
M,N = map(int, input().split())

num = []
#初始化为0
for i in range(10):
    num.append(0)



def Count(n):
    global num
    tem = []
    tem.extend(str(n))
    for i in tem:
        num[int(i)] += 1

for i in range(M,N+1):
    #print(i)
    Count(i)
    #print(num)

for i in num:
    print(i,end=' ')