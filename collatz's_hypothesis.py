c0 = int(input("Enter number: "))
steps = 0

while c0 < 1:
    print("Enter non zero and non negative number")
    break

while c0 > 1:
    if c0 % 2 == 0:
        c0 = (c0 // 2)
        steps += 1
        print(c0)
    elif c0 % 2 == 1:
        c0 = 3 * c0 + 1
        steps += 1
        print(c0)

print("Steps =", steps)


