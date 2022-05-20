'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        merge=[]
        median=0
        len_nums1=len(nums1)
        len_nums2=len(nums2)
        while i<len_nums1 and j<len_nums2:
            if nums1[i]<=nums2[j]:
                merge.append(nums1[i])
                i+=1
            else:
                merge.append(nums2[j])
                j+=1
        while i<len_nums1:
            merge.append(nums1[i])
            i+=1
        while j<len_nums2:
            merge.append(nums2[j])
            j+=1
        len_merge=len(merge)
        if len_merge%2==0:
            median=(merge[len_merge//2]+merge[(len_merge//2)-1])/2
        else:
            median=merge[(len_merge//2)]
        return median
            
