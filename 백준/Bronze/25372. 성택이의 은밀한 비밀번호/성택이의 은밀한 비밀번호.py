n= int(input())
arr = [input() for _ in range(n)]

for i in arr:
    if len(i)>=6 and len(i)<=9:
        print('yes')
    else:
        print('no')