# def palindrom(s):
#     # s = ''.join(c for c in s if c.isalnum()).lower()
#     l=[]
#     for i in range(len(s)):
#         for j in (i+1,len(l)):
#             if s[i]==s[j]:
#                 l.append(s[i])
#         return ''.join(l)
#     return None
# print(palindrom("cbbd"))
# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# code
def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return ""
    
    # Create a 2D array to store the palindrome status
    dp = [[False] * n for _ in range(n)]
    max_length = 1
    start = 0

    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True

    # Check for two-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for palindromes of length 3 or more
    for length in range(3, n + 1):  # length of the substring
        for i in range(n - length + 1):  # starting index of the substring
            j = i + length - 1  # ending index of the substring
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                if length > max_length:
                    max_length = length
                    start = i

    return s[start:start + max_length]

# Test the function
print(longest_palindrome("babad"))  # Output: "bab" or "aba"
