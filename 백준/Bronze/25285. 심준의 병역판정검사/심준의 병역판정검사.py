n= int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in arr:
    hei,wei = i[0],i[1]
    bmi=wei/((hei*0.01)**2)
    if hei<140.1:
        print(6)
    elif hei>=204:
        print(4)
    elif hei>=140.1 and hei<146:
        print(5)
    elif hei>=146 and hei<159:
        print(4)
    elif hei>=159 and hei<161:
        if bmi>=16.0 and bmi<35.0:
            print(3)
        else:
            print(4)
    else:
        if bmi>=20.0 and bmi<25.0:
            print(1)
        elif bmi>=18.5 and bmi<20.0:
            print(2)
        elif bmi>=25.0 and bmi<30.0:
            print(2)
        elif bmi>=16.0 and bmi<18.5:
            print(3)
        elif  bmi>=30.0 and bmi<35.0:
            print(3)
        else:
            print(4)