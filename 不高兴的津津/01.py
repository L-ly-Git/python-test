n = int(input())

unhappy = []
index = 0
def Unhappy(s,c):
    global unhappy,index
    if index == 0:
        unhappy.append(s+c-8)
    else:
        unhappy.append(unhappy[index-1]+s+c-8)
    index+=1


for i in range(n):
   # 输入
    s,c = map(int,input().split())
   # 计算时间
    Unhappy(s,c)


#print(unhappy)

sum = 0
for i in unhappy:
    sum += i

print(sum)