# Delete Duplicate Folders in System

import collections
class Folder:
    def __init__(self,v):
        self.val = v
        self.deleted = False
        self.subfolders = {}
    
class Solution:
    def deleteDuplicateFolder(self, paths):
        root = Folder("/")

        def add(path):
            current = root
            for d in path:
                if d not in current.subfolders:
                    current.subfolders[d] = Folder(d)
                current = current.subfolders[d]
        
        def merge_hash(arr):
            return hash("".join(str(x) for x in arr))
        
        lookup = collections.defaultdict(list)
        def populate_hash(node):
            hashes = []
            for f in sorted(node.subfolders.keys()):
                hashes.append(populate_hash(node.subfolders[f]))    
            h = merge_hash(hashes)
            if len(node.subfolders.keys()) > 0:
                lookup[h].append(node)
            return hash(str(h) + str(hash(node.val)))
                 
        for path in paths:
            add(path)
        
        populate_hash(root)
        
        for h in lookup.keys():
            if len(lookup[h]) > 1:
                for node in lookup[h]:
                    node.deleted = True

        ans = []
        def traverse(node, path):
            if node.deleted:
                return

            if len(path) > 0:
                ans.append(path[:])
            for f in node.subfolders:
                path.append(f)
                traverse(node.subfolders[f], path)
                path.pop()
        
        traverse(root, [])
        return ans