li = [2,3,5,6,7,3,1,4,5,9,0,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5]
for i in range(len(li)):
    sorted = True
    for j in range(len(li)-i-1):
        if li[j] > li[j+1]:
            li[j],li[j+1] = li[j+1],li[j]
            sorted = False
    if sorted: break
print (li)