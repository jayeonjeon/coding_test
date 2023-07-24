max_num=0
num=0
for _ in range(10):
    n, m = map(int,input().split())
    num=num-n+m
    if max_num<num:
        max_num=num
print(max_num)