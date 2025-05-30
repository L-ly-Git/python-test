
matrix = []  #二阶列表

row = []
row.extend(input()) #第一行
#print(row)
matrix.append(row)

N = len(row)   #得到列数

for i in range(N-1):     #在输入，N -1 行 ，得到N*N列表（矩阵）
    row = []
    row.extend(input())  # 第一行
   # print(row)
    matrix.append(row)

#print(matrix)

def Jie_Ya(matrix,N):      #解压缩
    li = []
    li.append(N)      #第一位记录阶数
    num_zero = 0
    num_one = 0
    n = 0         #判断当前记录0或1
    Row = 1       #记录当前行数
    for row in matrix:
    #    print(row)
        index = 1
        for x in row:
            #print(row)
  #          print(x,end=' ')
            if n%2 ==0: #n为偶数，记录0个数
                if x == '0':       #是0 个数加一
                    num_zero += 1
                else:#是1或已经遍历完将个数存储进li
                    li.append(num_zero)
                    num_zero=0
                    num_one+=1
                    n+=1
            elif n%2 ==1:
                if x == '1':
                    num_one+=1
                else:
                    li.append(num_one)
                    num_one =0
                    num_zero+=1
                    n+=1

            index+=1
        Row+=1
    if n%2==0:
        li.append(num_zero)
    else:
        li.append(num_one)
    return li

li = Jie_Ya(matrix,N)

for i in li:
    print(i,end=' ')
