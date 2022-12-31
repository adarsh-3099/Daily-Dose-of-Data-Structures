class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        m = {}
        for i in range(len(nums2)):
            m[nums2[i]] = i
            
            
        for i in range(len(nums1)):
            r = m[nums1[i]]
            x = nums1[i]
            f = 1
            while r<len(nums2):
                if nums2[r] > x:
                    f = -1
                    break
                r += 1
            if f == -1:
                nums1[i] = nums2[r]
            else:
                nums1[i] = -1
        print(nums1)
        return nums1