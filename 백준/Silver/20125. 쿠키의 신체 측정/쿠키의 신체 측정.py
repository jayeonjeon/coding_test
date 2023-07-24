import sys

n=int(input())
chr=[sys.stdin.readline().strip() for i in range(n)]

x=0
for c in chr:
    if '*' in c:
        y=c.index('*')
        break
    x+=1

print(x+2, y+1)

l_arm = chr[x+1][0:y].count('*')
r_arm = chr[x+1][y+1:n+1].count('*')

waist=0
l_leg=0
r_leg=0

for i in range(2,n):
    if chr[x+i][y] == '*':
        waist+=1
    else:
        break

for i in range(2,n-x-waist):
    if chr[x+waist+i][y-1] == '*':
        l_leg+=1
    else:
        break

for i in range(2,n-x-waist):
    if chr[x+waist+i][y+1] == '*':
        r_leg+=1
    else:
        break

print(l_arm, r_arm, waist, l_leg, r_leg)