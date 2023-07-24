for _ in range(int(input())):
    n=int(input())
    n=format(n,'b')
    n=n[::-1]
    result=''
    for i, c in enumerate(n):
        if c=='1':
            result+=str(i)+' '
    print(result.rstrip(' '))