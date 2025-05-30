

N = int(input())

def If_Zhi(n):
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1

def Cal(N):
    for i in range(2,N):
        if If_Zhi(i)==1 and If_Zhi(N-i)==1:
            print(f"{N}={i}+{N-i}")
            break

for i in range(4,N+1):
    if i%2 == 0:
        Cal(i)