n=int(input())
arr = list(map(int,input().split()))

jw=arr[0]
arr=arr[1:]
arr=sorted(arr)

for i in range(len(arr)):
    if jw>arr[i]:
        jw+=arr[i]
    else:
        print('No')
        exit()
print('Yes')