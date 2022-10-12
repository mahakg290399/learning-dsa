from operator import le


inList = [9,5,3,2,6,8,3,9]
inSize = 3
maxSize = 0
for i in range(len(inList)+1-inSize):
    temp = sum(inList[i:i+inSize])
    if temp > maxSize:
        maxSize = temp
print(maxSize)
        