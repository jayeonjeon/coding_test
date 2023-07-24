dwarf = [int(input()) for _ in range(9)]
dwarf.sort()

a,b=0,0
for i in range(0,8):
    for j in range(i+1,9):
        if sum(dwarf)-(dwarf[i]+dwarf[j])==100:
            a,b=dwarf[i],dwarf[j]

dwarf.remove(a)
dwarf.remove(b)

for ans in dwarf:
    print(ans)