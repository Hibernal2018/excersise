data = [3, 2, 1, 7, 5, 11, 9]
n = len(data)

for i in range(n):
    swapped = False
    for j in range(n - i -1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
            swapped = True
    if swapped:
        continue
    else:
        print(data)
        break
