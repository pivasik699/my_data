import time
arr = []
f = [1,2]
arr.append(f[1])
while True:
      f[0] = f[0] + f[1]
      if f[0] % 2 == 0:
            arr.append(f[0])
      f[1] = f[0] + f[1]
      if f[1] % 2 == 0:
            arr.append(f[1])
      time.sleep(0.5)
      print arr
      if f[0] >= 4000000:
            print("gg")
            break
      if f[1] >= 3500000:
            print("gg")
            break
otvet = sum(arr)
print otvet
