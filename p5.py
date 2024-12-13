# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# code
# def lengthOfLongestSubstring(s: str) -> int:
#     if not s:
#         return 0
#     start = 0
#     max_len = 0
#     char_dict = {}
#     for end in range(len(s)):
#         if s[end] in char_dict and char_dict[s[end]] >= start:
#             start = char_dict[s[end]] + 1
#             char_dict[s[end]] = end
#             max_len = max(max_len, end - start + 1)
#         else:
#             char_dict[s[end]] = end
#             max_len = max(max_len, end - start + 1)
#     return max_len

# s=input("Enter a String: ")
# print(lengthOfLongestSubstring(s))

def fun(s):
    if not s:
        return 0
    start=0
    max_len=0
    char_dic={}
    for end in range(len(s)):
        if s[end] in char_dic and char_dic[s[end]]>=start:
            start=char_dic[s[end]]+1
            char_dic[s[end]]=end
            max_len=max(max_len,end-start+1)
        else:
            char_dic[s[end]]=end
            max_len=max(max_len,end-start+1)
    return max_len