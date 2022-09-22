li = [2,3,5,6,7,3,1,4,5,9,0,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5]

for i in range(len(li)):
    minPos = i
    for j in range(i, len(li)):
        if li[j] < li[minPos]: minPos = j 
    li[i], li[minPos] = li[minPos], li[i]

print(li)