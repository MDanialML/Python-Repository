l1 = [3,5,6,4,9,8,7]
lentght = len(l1)

for i in range(lentght-1):
    swapped = False
    for j in range(lentght-i-1):
        if(l1[j] > l1[j+1]):
            temp = l1[j]
            l1[j] = l1[j+1]
            l1[j+1] = temp
            swapped = True
    if not swapped:
        break

print(l1)