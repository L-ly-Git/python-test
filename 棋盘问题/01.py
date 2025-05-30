#
# N,M =map(int,input().split())
# #N 行数  M 列数
# #生成一个N行M列的棋盘
# Num_Zheng = 0
# #计算正方形个数
# def Zheng(N,M,Line,Row):
#     if Line > M or Row > N:
#         return 0
#     global Num_Zheng
#     line = Line
#     row = Row
#     while row <= N:
#         if line == M:
#             while line >= Line:
#                 Num_Zheng += 1
#                 print(f'Num_Zheng={Num_Zheng},line={line},row={row}')
#                 line-=1
#             row+=1
#             line+=1
#         elif line == Line:
#             while line <= N:
#                 Num_Zheng += 1
#                 print(f'Num_Zheng={Num_Zheng},line={line},row={row}')
#                 line += 1
#             row += 1
#             line-=1
#     Line += 1
#     Row += 1
#     Zheng(N,M,Line,Row)
#
# Zheng(N,M,1,1)
#
# Num_Chang = 0
# def Chang(N,M,Line,Row):
#     global Num_Chang
#     line = Line
#     row = Row
#     while row <= M:
#         if line == N:
#             while line >= Line:
#                 Num_Zheng += 1
#                 print(f'Num_Chang={Num_Chang},line={line},row={row}')
#                 line-=1
#             row+=1
#             line+=1
#         elif line == 1:
#             while line <= N:
#                 Num_Zheng += 1
#                 print(f'Num_Chang={Num_Chang},line={line},row={row}')
#                 line += 1
#             row += 1
#             line-=1


# print(Num_Zheng)


# # 读取输入的矩阵行数 N 和列数 M
# N, M = map(int, input().split())
# # 初始化计数器
# Num_Zheng = 0
#
# def cal2(N,M,Col,Row):
#     global Num_Zheng
#     col = Col
#     row = Row
#     while col %2 == 0:
#
#
# def Zheng(N,M,Col,Row):
#     col = Col
#     row = Row
#     if col % 2 == 0: #偶数开始
#         Cal2(N,M,Col,Row)
#     else:           #奇数开始
#         Cal1(N,M,Col,Row)
#     #一次遍历结束，Row,Col +1
#     Col+=1
#     Row+=1
#     Zheng(N,M,Col,Row)
#
#
# # 按列遍历矩阵
# for col in range(M):
#     if col % 2 == 0:
#         # 偶数列从上到下遍历
#         for row in range(N):
#             Num_Zheng += 1
#     else:
#         # 奇数列从下到上遍历
#         for row in range(N - 1, -1, -1):
#             Num_Zheng += 1
#
# # 输出总的步数
# print(Num_Zheng)



#
# 计算正方形个数
# 对于一个 N 行 M 列的棋盘，边长为 k 的正方形个数的计算方法如下：
# 边长为 1 的正方形个数为 N * M。
# 边长为 2 的正方形个数为 (N - 1) * (M - 1)。
# 以此类推，边长最大为 min(N, M)。

# 计算长方形个数
# 长方形个数可以通过总矩形个数减去正方形个数得到。
# 总矩形个数的计算方法是从 N 行中选 2 行的组合数乘以从 M 列中选 2 列的组合数，
# 即 (N * (N + 1) * M * (M + 1)) // 4。

# 读取输入的行数 N 和列数 M
N, M = map(int, input().split())

# 计算正方形个数
Num_Zheng = 0
for k in range(1, min(N, M) + 1):
    Num_Zheng += (N - k + 1) * (M - k + 1)

# 计算长方形个数
total_rectangles = (N * (N + 1) * M * (M + 1)) // 4    #总矩形数，行列组合数相乘
Num_Chang = total_rectangles - Num_Zheng

# 输出结果
print(f"{Num_Zheng} {Num_Chang}")