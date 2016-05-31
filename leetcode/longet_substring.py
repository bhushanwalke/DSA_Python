import sys
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    length_string = len(s)
    if length_string <= 1:
        return s
    hash_map = {}
    max_length = 0
    curr_index = 0
    for i in range(length_string):
        if s[i] in hash_map and (max_length < len(s[curr_index: i])):
            max_length = len(s[curr_index: i])
            res = s[curr_index: i]
            curr_index = i
            hash_map = {}
        hash_map[s[i]] = i
    return max_length



print lengthOfLongestSubstring("abcabcbb")
print lengthOfLongestSubstring("pwwkew")
