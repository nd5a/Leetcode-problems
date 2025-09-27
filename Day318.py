# Largest Triangle Area

from math import sqrt
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        N = len(points)
        best = 0

        def dist(a, b):
            return sqrt((a[0] - b[0]) ** 2 + ((a[1] - b[1]) ** 2))
        

        def find_area(i, j, k):
            a = dist(points[i], points[j])
            b = dist(points[j], points[k])
            c = dist(points[k], points[i])

            s = (a + b + c) / 2
            return sqrt(s * max(s- a, 0) * max(s- b, 0) * max(s - c, 0))
        
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    best = max(best, find_area(i, j, k))
        return best