import math

n=int(input())
a=list(map(int,input().split()))

def primenumber(x):
    if x == 1:
	    return 0
    for i in range(2, int(math.sqrt(x) + 1)):	
    	if x % i == 0:		
        	return 0
    return 1

x=0
for i in a:
	x+=primenumber(i)
	
print(x)