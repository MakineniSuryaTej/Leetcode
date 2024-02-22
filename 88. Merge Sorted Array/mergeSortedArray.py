class Solution:
    def merge(self, nums1: List[int], n: int, nums2: List[int], m: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        newArray = []
        
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

        for i in range(0,len(newArray)):
            nums1[i] = newArray[i]
