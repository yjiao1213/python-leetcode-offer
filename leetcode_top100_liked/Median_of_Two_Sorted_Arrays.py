class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        
        imax, imin, mid = m, 0, (m+n+1)//2
        
        while imin<=imax:
            i = (imax+imin)//2
            j = mid-i
            
            if i>0 and nums2[j]<nums1[i-1]:
                imax = i-1
            elif i<m and nums1[i]<nums2[j-1]:
                imin = i+1
            else:
                if i==0:
                    lef_max = nums2[j-1]
                elif j==0:
                    lef_max = nums1[i-1]
                else:
                    lef_max = max(nums1[i-1], nums2[j-1])
                if (m+n)%2==1:
                    return lef_max
                
                if i==m:
                    right_min = nums2[j]
                elif j==n:
                    right_min = nums1[i]
                else:
                    right_min = min(nums1[i], nums2[j])
                return (lef_max+right_min)/2
        
