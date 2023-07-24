dwarf = [int(input()) for _ in range(9)]

nd1,nd2=0,0
for i in range(0,8):
    for j in range(i+1,9):
        if sum(dwarf)-dwarf[i]-dwarf[j]==100:
            nd1,nd2=dwarf[i],dwarf[j]

dwarf.remove(nd1)
dwarf.remove(nd2)

for dw in dwarf:
    print(dw)
