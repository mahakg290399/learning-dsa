# You are given two strings: pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

# Your task is to calculate the number of substrings of source that match pattern. 

# We’ll say that a substring source[l..r] matches pattern if the following three conditions are met:
# – The pattern and substring are equal in length.
# – Where there is a 0 in the pattern, there is a vowel in the substring. 
# – Where there is a 1 in the pattern, there is a consonant in the substring. 

# Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.

# Example

# For pattern = "010" and source = "amazing", the output should be solution(pattern, source) = 2.
# – “010” matches source[0..2] = "ama". The pattern specifies “vowel, consonant, vowel”. “ama” matches this pattern: 0 matches a, 1 matches m, and 0 matches a. 
# – “010” doesn’t match source[1..3] = "maz" 
# – “010” matches source[2..4] = "azi" 
# – “010” doesn’t match source[3..5] = "zin" 
# – “010” doesn’t match source[4..6] = "ing"

# So, there are 2 matches. For a visual demonstration, see the example video. 

# For pattern = "100" and source = "codesignal", the output should be solution(pattern, source) = 0.
# – There are no double vowels in the string "codesignal", so it’s not possible for any of its substrings to match this pattern.

# Guaranteed constraints:
# 1 ≤ source.length ≤ 103
# 1 ≤ pattern.length ≤ 103

def pattern_matching(pattern, source):
    # Use set for O(1) lookup of vowels
    vowels = set('aeiouy')
    
    # Length validation
    pattern_len = len(pattern)
    source_len = len(source)
    if pattern_len > source_len:
        return 0
    
    # Pre-compute character type array for source string
    # True for vowel, False for consonant
    char_types = [c in vowels for c in source]
    
    # Convert pattern to boolean array (0->True for vowel, 1->False for consonant)
    pattern_types = [c == '0' for c in pattern]
    
    count = 0
    # Sliding window approach
    for i in range(source_len - pattern_len + 1):
        # Compare boolean arrays directly
        if all(char_types[i + j] == pattern_types[j] for j in range(pattern_len)):
            count += 1
            
    return count

pattern1 = "010"
pattern2 = "100"
source1 = "amazing"
source2 = "Somethiing"
print(pattern_matching(pattern1, source1))
print(pattern_matching(pattern2, source2))
