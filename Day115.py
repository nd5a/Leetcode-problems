# Merge Two 2D Arrays by Summing Values

class Solution:
    def mergeArrays(self, nums1, nums2):
        N1 = len(nums1)
        N2 = len(nums2)

        index1 = 0
        index2 =0
        ans =[]
        while index1 < N1 and index2 < N2:
            if nums1[index1][0] == nums2[index2][0]:
                ans.append((nums1[index1][0], nums1[index1][1] + nums2[index2][1]))
                index1 +=1
                index2 +=1
            elif nums1[index1][0] > nums2[index2][0]:
                ans.append((nums2[index2][0], nums2[index2][1]))
                index2 +=1
            else:
                ans.append((nums1[index1][0], nums1[index1][1]))
                index1 +=1
        
        while index1 < N1:
            ans.append(nums1[index1])
            index1+= 1
        
        while index2< N2:
            ans.append(nums2[index2])
            index2 += 1

        return ans