str = input()
str = str.lower()
li_str=list(set(str))

fre=[]
for s in li_str:
    fre.append(str.count(s))

if len(fre)>=2:
    if sorted(fre, reverse=True)[0] ==  sorted(fre, reverse=True)[1]:
        print('?')
    else:
        idx=fre.index(sorted(fre, reverse=True)[0])
        print(li_str[idx].upper())
else:
    idx=fre.index(sorted(fre, reverse=True)[0])
    print(li_str[idx].upper())