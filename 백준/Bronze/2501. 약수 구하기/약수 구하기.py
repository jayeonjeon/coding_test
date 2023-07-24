n, m = map(int, input().split())

divisior=[]
for i in range(1,n+1):
    if n%i==0:
        divisior.append(i)

try:
    print(divisior[m-1])
except:
    print(0)