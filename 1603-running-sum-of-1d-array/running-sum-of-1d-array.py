class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            arr.append(sum)
        return arr
        