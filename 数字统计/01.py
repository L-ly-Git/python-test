

def Count(Num):
    count = 0
    while Num > 0:
       # print(Num)
        tem = Num%10
        if tem == 2:
            count+=1
        Num //= 10
    return count


#print(Count(222))

L,R = map(int,input().split())
#print(L,R)
#
count = 0
for i in range(L,R+1):
    count += Count(i)

print(count)