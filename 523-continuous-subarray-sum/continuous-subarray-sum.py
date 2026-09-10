class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ps=0
        freq={0:-1}
        for i,num in enumerate(nums):
            ps+=num
            n=ps%k
            if n in freq:
                s=i-freq[n]
                if s>=2:
                    return True
            else:
                freq[n]=i
        return False