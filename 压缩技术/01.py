

#
# N,*li = map(int,input().split())
# #li1 = list(*li)
#
# matrix = []      #二维数组存储
# def Ya(list,N):
#     count = 0
#     n = 0
#     for i in list:
#        # print(f'i = {i}')
#         if n%2==0:
#             for j in range(i):
#                 print('0',end='')
#                 count+=1
#                 if count == N:
#                     print('\n')
#                     count=0
#             n+=1
#         elif n%2==1:
#             for j in range(i):
#                 print('1',end='')
#                 count+=1
#                 if count == N:
#                     print('\n')
#                     count=0
#             n+=1
#
# Ya(li,N)





N,*li = map(int,input().split())
#li1 = list(*li)


matrix = []      #二维列表存储
def Ya(list,N):
    n = 0
    Row = 0
    while(Row<N):
        row = []
        for i in list:
            # print(f'i = {i}')
            if n % 2 == 0:
                for j in range(i):
                    row.append('0')
                    if len(row)==N:
                        matrix.append(row)
                        row = []
                        Row+=1
                n += 1
            elif n % 2 == 1:
                for j in range(i):
                    row.append('1')
                    if len(row)==N:
                        matrix.append(row)
                        row = []
                        Row+=1
                n += 1


def Print(matrix):
    for row in matrix:
        print(''.join(str(x) for x in row))



Ya(li,N)
Print(matrix)

