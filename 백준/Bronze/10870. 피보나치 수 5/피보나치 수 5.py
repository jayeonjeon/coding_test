fb=[0,1]
for i in range(0,21):
    fb.append(fb[i]+fb[i+1])

print(fb[int(input())])