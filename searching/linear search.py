def linear_search(list,target):
    """
    return the index position of the target if found, else returns None
    """
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [x for x in range(1,100000001)]
print("Done with numbers")
result = linear_search(numbers,100000000)
verify(result)
