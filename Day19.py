class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        arr = []
        for row in matrix:
            arr.extend(row)
        arr.sort()

        N = len(arr)
        for i in range(0,N,2):
            if not (i + 1 < N):
                break
            if arr[i] < 0 and arr[i+1]<0:
                arr[i] *= -1
                arr[i+1] *= -1
            elif arr[i]<0 and arr[i+1]>= 0 and arr[i]+ arr[i+1]<0:
                arr[i] *= -1
                arr[i + 1] *=-1

        return sum(arr)