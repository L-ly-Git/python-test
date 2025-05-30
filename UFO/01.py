Group = input()
Plate = input()

def Cal(str):
    result = 1
    for i in str:
        result *= (ord(i)-64)
    return result%47

if Cal(Group) == Cal(Plate):
    print("GO")
else:
    print("STAY")