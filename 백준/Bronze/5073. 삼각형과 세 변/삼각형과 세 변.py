arr=[]
while (1):
    a,b,c=map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        arr.append([a,b,c])

for a in arr:
    a,b,c=sorted(a,reverse=True)
    if a >= b+c:
        print("Invalid")
    elif a==b==c:
        print("Equilateral")    
    elif a==b or b==c or c==a:
        print("Isosceles")
    else:
        print("Scalene")