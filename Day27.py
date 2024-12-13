# # Check if a word occurs as a prefix of any word in a sentence

# def isprefixWord(sentence, searchWord):
#     words = sentence.split(" ")
    
#     for i in range(len(words)):
#         if words[i].startswith(searchWord):
#             return i + 1
#     else:
#         return -1
# k = 7
# arr = [1, 8, 10, 6 ,4 ,6, 9, 1]
# def getMinDiff(arr,k):
#         # code here
#         arr.sort()
#         n = len(arr)

#         result = arr[n - 1] - arr[0]

#         for i in range(1, n):
#             if arr[i] - k < 0:
#                 continue

#             max_height = max(arr[i - 1] + k, arr[n - 1] - k)
#             min_height = min(arr[0] + k, arr[i] - k)
#             result = min(result, max_height - min_height)
#         return result
# print(getMinDiff(arr, k))

arr = [2,3,-8,7,-1,2,3]
l=[]
for i in range(len(arr)):
    if len(arr) == 1:
        l.append(arr[i])
    for j in range(i+1,len(arr)+1):
        l.append(sum(arr[i:j]))
        
print(max(l))