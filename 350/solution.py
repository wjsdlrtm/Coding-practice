class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result = []
        temp = []
        while 1:
            temp = list(set(nums1).intersection(set(nums2)))
            if not temp:
                break
            for i in temp:
                nums1.remove(i)
                nums2.remove(i)
            result += temp
        return result