# Maximum Area of Longest Diagonal Rectangle

class Solution:
    def areaOfMaxDiagonal(self, dimensions):
        N = len(dimensions)

        long_diag = -1
        biggest_area = -1

        for w, h in dimensions:
            d2 = w * w + h * h
            if d2 > long_diag:
                long_diag = d2
                biggest_area = w * h
            elif d2 == long_diag and biggest_area < w * h:
                biggest_area = w *h
        return biggest_area