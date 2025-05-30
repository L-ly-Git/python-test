
n = int(input())

li = list(map(int,input().split()))

def Max_Link(list,n):
    Max_Count = 1
    count = 1
    for i in range(n-1):
        #print(list[i],list[i+1])
        if list[i]+1 == list[i+1]:
            count +=1
         #   print(count)
        else:
            if count > Max_Count:
                Max_Count = count
            count = 1
    if count > Max_Count:
        Max_Count = count
    return Max_Count

Max_Count = Max_Link(li,n)

print(Max_Count)