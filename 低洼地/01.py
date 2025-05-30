

n = int(input())



li = list(map(int,input().split()))

#print(li)

def If_Can(list,n):
    count = 0
    i = 1
    while i < n-1:
        if li[i]<li[i-1]:
            if li[i]<li[i+1]:
                count+=1
                i += 1
            elif li[i] == li[i+1]:
               # print(i)
                i+=1
                while i < n-1:
                #    print(i)
                    if li[i]<li[i+1]:
                        count+=1
                        i+=1
                        break
                    elif li[i]==li[i+1]:
                        i+=1
                    else:
                        i+=1
                        break
            else:
                i+=1
        else:
            i+=1
    return count

count = If_Can(li,n)

print(count)

