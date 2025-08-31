# Given two sorted lists, write a function to merge them into one sorted list.

# Bonus: What’s the time complexity?

# Example:

# Input:

# list1 = [1,2,5]
# list2 = [2,4,6]
# Output:

# def merge_list(list1,list2) -> [1,2,2,4,5,6]

def merge_list(list1:list, list2:list):
    # if len(list1)> len(list2): remaining = list1[len(list2):]
    result = []
    short_list = list1
    if len(list1) > len(list2):
        short_list = list2
    while len(short_list) > 0:
        if list1[0] > list2[0]:
            result.append(list2.pop(0))
        else:
            result.append(list1.pop(0))
    if len(list1) > 0:
        result.extend(list1)
    if len(list2)>0:
        result.extend(list2)
    return result

list1 = [1,2,5, 10]
list2 = [2,4,6]
print(merge_list(list1, list2))