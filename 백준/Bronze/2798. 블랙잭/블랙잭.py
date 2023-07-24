n, m = map(int, input().split())
card = list(map(int,input().split()))

blcjack = 0

for i in range(1,n-1):
    for j in range(i+1,n):
        for k in range(j+1,n+1):
            sum_card=card[i-1]+card[j-1]+card[k-1]
            if sum_card<=m and blcjack<sum_card:
                blcjack=sum_card
print(blcjack)