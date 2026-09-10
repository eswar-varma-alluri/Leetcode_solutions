class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n3=nums1+nums2
        n3.sort()
        mid=len(n3)//2
        if len(n3)%2!=0:
            return n3[mid]
        else:
            return float((n3[mid]+n3[mid-1])/2)