a= [list(map(int,input().split())) for _ in range(int(input()))]
for i in a:
    i=sorted(i)
    print(i[-3])