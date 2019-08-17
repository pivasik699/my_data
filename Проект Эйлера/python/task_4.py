y = 100
x = 100
z = 0
m = []
while True:
    x+=1
    if x == 1000:
        y+=1
        x-= 900
    z = x * y
    z = str(z)
    if len(z) == 6:
        if int(z[0]) == int(z[-1]):
            if int(z[1]) == int(z[-2]):
                if int(z[2]) == int(z[-3]):
                    m.append(z)
                    print max(m)
    if y == 1000:
        print('Самое большое число:' + max(m))
        break
