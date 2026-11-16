s = "tabbaj"

# Brute force: check every substring, O(n^3) time
longest = ""

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        temp = s[i:j]
        if temp == temp[::-1] and len(temp) > len(longest):
            longest = temp

print(longest)

# Optimal: expand around every center, O(n^2) time, O(1) space
def expand(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

longest = ""

for i in range(len(s)):
    odd = expand(i, i)
    even = expand(i, i + 1)
    if len(odd) > len(longest):
        longest = odd
    if len(even) > len(longest):
        longest = even

print(longest)
