
N = int(input())
#print(N,type(N))
count = 1
def Cal_Wei(N):
    global count
    N = abs(N)
  #  print(N)
    while N >= 10:
        N //= 10
        count *= 10
    return count

Cal_Wei(N)      #得到N的位数



def Redown(N,count):
    Re_N = 0
    cou = 1
    while count > 0:
       # print(count)
        # print(N)
        tep = N//count
        Re_N += tep*cou
        N %= count
        count = count//10
        cou *= 10
    return Re_N
if N > 0:
   print(Redown(abs(N),count))
else:
    print(-Redown(abs(N),count))