


def Input():
    src = input()   #输入字符串

    #以‘/’分割
    li_src = src.split('/')

    #转换为整数
    li_int = [int(li_src[0]),int(li_src[1])]

    return li_int

li1 = Input()

li2 = Input()

#求最大公约数
def Gong(n,m):
    r = n%m
   # print(n,m,r)
    if r == 0:
     #   print(m)
        return m
    else:
        return Gong(m,r)

#化简
def Line_Row(n,m):
    #n为分子，m为分母
    r = Gong(n,m)  #最大公约数
    row = n//r
    line = m//r
    li = [line,row]
    return li

#分子乘积
Time_Zi = li1[0]*li2[0]
#分母乘积
Tine_Mu = li1[1]*li2[1]

li = Line_Row(Time_Zi,Tine_Mu)

for i in li:
    print(i,end = ' ')

