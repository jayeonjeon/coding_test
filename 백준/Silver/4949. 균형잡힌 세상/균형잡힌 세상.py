while True:
    s = input()
    if s == ".":
        break
    stack = []
    d = {")": "(", "]": "["}
    printed = False
    for char in s:
        if char in list(d.values()):
            stack.append(char)
            continue
        if char in d:
            try:
                if stack.pop() != d[char]:
                    print("no")
                    printed = True
                    break
            except:
                print("no")
                printed = True
                break
    if printed:
        continue
    if len(stack) == 0:
        print("yes")
        continue
    print("no")