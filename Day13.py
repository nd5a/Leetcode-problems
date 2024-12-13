# def decrypt(code, k):
#     """
#     :type code: List[int]
#     :type k: int
#     :rtype: List[int]
#     """
#     n = len(code)
    
#     # If k == 0, replace all numbers with 0
#     if k == 0:
#         return [0] * n
    
#     # Extend the circular array for easy calculation
#     extended_code = code * 2
#     result = []
    
#     if k > 0:  # Sum of the next k numbers
#         for i in range(n):
#             result.append(sum(extended_code[i + 1:i + 1 + k]))
#     elif k < 0:  # Sum of the previous k numbers
#         k = abs(k)
#         for i in range(n):
#             result.append(sum(extended_code[n + i - k:n + i]))
    
#     return result

# # Test Cases
# print(decrypt([5, 7, 1, 4], 3))  # Output: [12, 10, 16, 13]
# print(decrypt([1, 2, 3, 4], 0))  # Output: [0, 0, 0, 0]
# print(decrypt([2, 4, 9, 3], -2))  # Output: [12, 5, 6, 13]

