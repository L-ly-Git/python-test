
import re

str = input()
num_boy =0
num_girl =0
#找boy
#（1)找boy连着三个
Res = re.findall('boy',str)
num_boy += len(Res)
#print(Res)
#将boy替换掉
Res = re.sub('boy','...',str)
#print(Res)
str = Res
#(2)找连着两个的
#bo
Res = re.findall('bo',str)
#print(Res)
num_boy+=len(Res)
#替换
Res = re.sub('bo','..',str)
#print(Res)
str = Res
#oy
Res = re.findall('oy',str)
#print(Res)
num_boy+=len(Res)
#替换
Res = re.sub('oy','..',str)
#print(Res)
str = Res

#找单个的
Res = re.findall('[boy]',str)
#print(Res)
num_boy+=len(Res)

#girl
#找四个连着
Res = re.findall('girl',str)
#print(Res)
num_girl+=len(Res)
#替换
Res = re.sub('girl','....',str)
#print(Res)
str = Res
#三个
#gir
Res = re.findall('gir',str)
#print(Res)
num_girl+=len(Res)
#替换
Res = re.sub('gir','...',str)
#print(Res)
str = Res
#irl
Res = re.findall('irl',str)
#print(Res)
num_girl+=len(Res)
#替换
Res = re.sub('irl','...',str)
#print(Res)
str = Res
#两个
# #gi
Res = re.findall('gi',str)
#print(Res)
num_girl+=len(Res)
#替换
Res = re.sub('gi','...',str)
#print(Res)
str = Res
#ir
Res = re.findall('ir',str)
#print(Res)
num_girl+=len(Res)
#替换
Res = re.sub('ir','...',str)
#print(Res)
str = Res
#rl
Res = re.findall('rl',str)
#print(Res)
num_girl+=len(Res)
#替换
Res = re.sub('rl','...',str)
#print(Res)
str = Res


#单个
Res = re.findall('[girl]',str)
#print(Res)
num_girl+=len(Res)

#输出
print(num_boy)
print(num_girl)