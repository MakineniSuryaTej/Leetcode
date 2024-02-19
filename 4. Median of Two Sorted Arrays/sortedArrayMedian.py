class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newArray = []
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                newArray.append(nums1[i])
                i += 1
            else:
                newArray.append(nums2[j])
                j += 1
        while i < n:
            newArray.append(nums1[i])
            i += 1
        
        while j < m:
            newArray.append(nums2[j])
            j += 1
        
        l = len(newArray)
        m = l // 2
        if l%2 == 0:
            return (newArray[m - 1] + newArray[m])/2
        else:
            return newArray[m]
