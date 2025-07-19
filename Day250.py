# Remove Sub-Folders from the Filesystem

class Solution:
    def removeSubfolders(self, folder):
        folder.sort()
        result = []

        for f in folder:
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)

        return result