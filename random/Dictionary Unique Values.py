# You are given a dictionary with a key-value of {string: number} where values in the dictionary could be duplicates. You are required to extract the unique values from the dictionary where the value occurred only once.

# Return a list of values where they occur only once.

# Note: You can return the values in any order.

# Input:

# dictionary = {"key1": 1, "key2": 1, "key3": 7, "key4": 3, "key5": 4, "key6": 7}
# Output:

# find_unique_values(dictionary) -> [3,4]

def find_unique_value(dictionary:dict):
    seen = set()
    temp = dict()
    for _, value in dictionary.items():
        if value in seen:
            temp[value] += 1
        else:
            temp[value] = 1
            seen.add(value)
    return [x for x,y in temp.items() if y == 1]
    

dictionary = {"key1": 1, "key2": 1, "key3": 7, "key4": 3, "key5": 4, "key6": 7}
print(find_unique_value(dictionary))