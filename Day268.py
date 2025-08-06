# Fruits Into Baskets III

NEG = -10**18

class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        if n == 0:
            return 0
        size = 1
        while size < n:
            size *= 2
        tree = [NEG] * (2 * size)
        for i in range(n):
            tree[size + i] = baskets[i]
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])
        
        def update(i):
            idx = size + i
            tree[idx] = NEG
            idx //= 2
            while idx:
                tree[idx] = max(tree[2 * idx], tree[2 * idx + 1])
                idx //= 2
        
        def query(x):
            if tree[1] < x:
                return -1
            node = 1
            while node < size:
                left = 2 * node
                right = 2 * node + 1
                if tree[left] >= x:
                    node = left
                else:
                    node = right
            return node - size
        
        unplaced = 0
        for x in fruits:
            idx = query(x)
            if idx == -1:
                unplaced += 1
            else:
                update(idx)
        return unplaced