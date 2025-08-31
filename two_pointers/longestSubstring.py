
def max_repeating(strr):
    right = strr[0]
    subset = strr[0]
    longest = (1,)
    for idx in range(1, len(strr)):
        if strr[idx] == right:
            right = strr[idx]
            subset += strr[idx]
        else:
            if longest[0]<len(subset):
                longest = len(subset), right
            right = strr[idx]
            subset = strr[idx]
    return longest[1]

print(max_repeating('adccccbbbbc'))
