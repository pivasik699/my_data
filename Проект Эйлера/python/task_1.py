x = 1000
i = 0
y = 0
z =[]
while i <= x:
    i+=3
    z.append(i)
    if i == 999:
        break
while y <= x:
    y+=5
    z.append(y)
    if y == 995:
        break
otvet = set(z)
otvet = sum(otvet)
print otvet
