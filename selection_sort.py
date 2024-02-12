li = [64, 34, 25, 5, 22, 11, 90, 12]

length = len(li)
for i in range(length-1):
    min_index = i
    for j in range(i+1,length):
        if(li[j] < li[min_index]):
            min_index = j
    element = li.pop(min_index)
    li.insert(i,element)

print("SOrted array",li)